#nvda-addonWizard: An addon generation template for NVDA.
#Copyright (C) 2016 on behalf of the NVDA community by Derek Riemer.
#see https://github.com/nvdaaddons/addonWizzard for more info.
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#This file initializes cookiecutter for your addon generation process.

from __future__ import print_function
import sys
import os
from collections import OrderedDict
from cookiecutter.main import cookiecutter

#Monkey patch to make input work on both python2 and python 3 the same.
if sys.version.startswith("2"):
	eval = input
	input = raw_input
	
	authors = None
	
	def authorFilter(string):
		global authors
		authors = string.split(",")
		authors = [i.strip() for i in authors]

def emailAndAuthorFilter(string):
	emails = string.split(",")
	emails = [i.strip() for i in emails] 
	while len(emails) < len(authors):
		emails.append("")
	both = zip(authors, emails)
	print(both)
	bothStrings = []
	for i in both:
		if i[1]:
			bothStrings.append("{0} <{1}>".format(*i))
		else:
			bothStrings.append(i[0])
		print(bothStrings)
	#bothStrings = [("{0} <{1}>".format(*i) if i[1] else i[0]) for i in both]
	if len(bothStrings) == 1:
		return bothStrings[0]
	else:
		bothStrings[-1]  = "and "+bothStrings[-1]
		return ", ".join(bothStrings)
"""Fields +explained.
List of these.
{
	"prompt":"prompt text",
	"default" : "default-text" (Not required),
	"exportToCookieCutterTemplateAs" :  (Must be pythonic variable valid string) ("doNotExport"  doesn't put it in the context at all),
	"filter" : FilterFunction (Not required),
)
"""
promptData = (
	{
		"prompt" : "Author Name: seperate multiple with commas",
		"default" : "John Doe",
		"exportToCookieCutterTemplateAs" : "doNotExport",
		"filter" : authorFilter,
	},
	{
		"prompt" : "Author Emails: Seperate multiple with commas. Optional",
		"filter" : emailAndAuthorFilter,
		"exportToCookieCutterTemplateAs" : "authorString",
	},
	{
		"prompt" : "Project Name: Can have spaces.",
		"default" : "Simple Addon",
		"exportToCookieCutterTemplateAs" : "projectName",
	},
	{
		"prompt" : "Addon Name: Must be valid python name",
		"default" : "simpleAddon",
		"exportToCookieCutterTemplateAs" : "addonName",
	},
	{
		"prompt" : """Addon Summary
		This text shows up in the add-ons manager for the add-ons name. Keep it short, it's the user facing name.""",
		"default" : "Simple Addon",
		"exportToCookieCutterTemplateAs" : "addonSummary",
	},
	{
		"prompt" : """Addon Description
		The add-on description can be edited later from buildVars.py, because it may be longer than one line.""",
		"default" : "This is my first add-on. It currently does nothing.",
		"exportToCookieCutterTemplateAs" : "addonDescription",
	},
	{
		"prompt" : """Add-on Version
		Either something like 1.0.0, 1.0.0-dev, or a date based version (16.07, or 16.07.1).""",
		"default" : "0.1.0-dev",
		"exportToCookieCutterTemplateAs" : "version",
	},
	{
		"prompt" : "If you have an add-on URL, type it here. Otherwise, press enter.",
		"default" : "None",
		"exportToCookieCutterTemplateAs" : "addonURL",
	},
	{
		"prompt" : "Do you want a globalPlugin skeleton generated for you, (y/n)",
		"default" : "y",
		"exportToCookieCutterTemplateAs" : "createGlobalPlugin",
	},
	{
		"prompt" : "Do you want an appModule skeleton generated for you? (Y/N).", 
		"default" : "y",
		"exportToCookieCutterTemplateAs" : "createAppModule",
	},
	{
		"prompt" : """Use continuous integration with Travis CI?
		Please see the readme to learn more.""",
		"default" : "n",
		"exportToCookieCutterTemplateAs" : "useContinuousIntegrationWithTravisCI",
	},
)
def getInput(prompt, default = ""):
	answer = ""
	while answer == "":
		print(prompt)
		answer = input(default)
		if answer == "":
			answer = default
		if default in ['y', 'n']:
			if answer.lower() not in ["y", "n", "yes", "no"]:
				print("Please answer yes or no.")
				continue
	return answer

def run():
	context = {}
	for item in promptData:
		resolvedItem = getInput(item["prompt"], item.get("default", ""))
		resolvedItem = item.get("filter", lambda str:str)(resolvedItem)
		contextKey = item["exportToCookieCutterTemplateAs"]
		if contextKey == "doNotExport":
			continue
		context[contextKey] =  resolvedItem

	context["project_slug"] = ("_".join(context["projectName"].split()) if " " in context["projectName"] else context["projectName"])
	curFileDir = os.path.join(os.path.dirname(__file__), "data")
	cookiecutter(curFileDir, no_input=True, extra_context=context)