from distutils.core import setup
import os

#http://stackoverflow.com/questions/27664504/how-to-add-package-data-recursively-in-python-setup-py
def package_files(directory):
	paths = []
	for (path, directories, filenames) in os.walk(directory):
		for filename in filenames:
			paths.append(os.path.join('..', path, filename))
	return paths

setup(name='NVDA-addonTemplate',
	version="0.5.1",
	description='Add-on template for writing NVDA add-ons',
	author='Derek Riemer and NVDA contributers',
	author_email='nvda-addons@freelists.org',
	url='http://addons.nvda-project.org',
	install_requires = [
		"cookiecutter",
		"markdown",
	],
	packages=[
		"NVDAAddonTemplate",
	],
	package_data={
		'NVDAAddonTemplate': package_files('NVDAAddonTemplate')
	},

	entry_points={
		'console_scripts': [
			"NVDAAddonTemplate = NVDAAddonTemplate:run",
		],
	}
)