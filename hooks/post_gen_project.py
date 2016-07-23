#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import shutil
from os.path import join as pathjoin
import glob
import datetime
from cookiecutter.main import cookiecutter
#evil monkeypatch. Fix for python 2 input
if sys.version.startswith("2"):
	eval = input
	input = raw_input

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
subTemplates = [
	(pathjoin("addon", "globalPlugins"), []),
	(pathjoin("addon", "appModules"), ("executableName",)),
	#add to me when more plugin types are needed.
]
context = {
	"copyrightYear" : datetime.datetime.now().year,
	"authorName" : "{{ cookiecutter.authorName }}",
	"projectName" : "{{ cookiecutter.projectName }}",
	"addonName" : "{{ cookiecutter.addonName }}",
	"addonURL" : "{{ cookiecutter.addonURL }}",
}

def getInput(arg):
	while True:
		print(arg)
		d = input()
		if d != "":
			return d
		print("Invalid input")

def renameFile(file, repl):
	file, repl = pathjoin(PROJECT_DIRECTORY, file), pathjoin(PROJECT_DIRECTORY, repl)
	os.rename(file, repl)

def removeAllTrees(theGlob):
	"""Takes   a glob expression, and removes all trees that match the glob. """
	#Start out under project_directory.
	theGlob = pathjoin(PROJECT_DIRECTORY, theGlob)
	dirs = glob.iglob(theGlob)
	for dir in dirs:
		removeTree(dir, False)

def removeTree(filepath, addProjDir=True):
	base = ("" if not addProjDir else PROJECT_DIRECTORY)
	dir = pathjoin(base, filepath)
	try:
		if os.path.isdir(dir):
			shutil.rmtree(dir)
		elif os.path.isfile(dir):
			os.remove(dir)
	except WindowsError:
		print("Something went wrong. Check", dir)
		


if __name__ == '__main__':
	if '{{ cookiecutter.useContinuousIntegrationWithTravisCI}}' != 'y':
		removeTree('appVeyor.yml')
		removeAllTrees("scons*")
	else:
		print("Please visit appVeyor.yml for some instructions.")

	if '{{ cookiecutter.createGlobalPlugin }}' != 'y':
		removeTree(pathjoin("addon", "globalPlugins"))

	if '{{ cookiecutter.createAppModule }}' != 'y':
		removeTree(pathjoin("addon", "appModules"))

	# Go through addon, and run cookieCutter on the inner projects.
	#Provide a whiteList in cookies to run cookieCutter on, I.E. globalPlugins doesn't require a cookie cutter to customize this, but appModules does.
	for (template, extra) in ((pathjoin(PROJECT_DIRECTORY, i[0], "template"), i[1]) for i in subTemplates):
		clonedContext = context.copy()
		for arg in extra:
			clonedContext[arg] = getInput(arg)
		if os.path.exists(template):
			cookiecutter(template , extra_context = clonedContext, output_dir=pathjoin(template, ".."), no_input=True)
			removeTree(template, False)
	
	#Necessary to rename the sconsstruct only because we remove scons*if they don't want appVeyor.
	renameFile(".sconstruct", "sconstruct")
	