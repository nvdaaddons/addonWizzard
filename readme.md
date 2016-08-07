# NVDA Add-on Scons Template  wizzard #

This package contains a command line wizard to create a basic template structure for NVDA add-on development, building, distribution and localization.
For details about NVDA add-on development please see the [NVDA Developer Guide](http://www.nvda-project.org/documentation/developerGuide.html).
The NVDA addon development/discussion list [is here](http://www.freelists.org/list/nvda-addons). 
Unless you wish to work on this template, I.E. update things, there is no need to clone this repository to simply create the basic structure of your addon.

Copyright (C) 2012-2016 nvda addon team contributors.

This package is distributed under the terms of the GNU General Public License, version 2 or later. Please see the file COPYING.txt for further details.

## Features

This template provides the following features you can use to help with NVDA add-on development:

*	Automatic add-on package creation, with naming and version loaded from a centralized build variables file (buildVars.py).
*	Manifest file creation using a template (manifest.ini.tpl). Build variables are replaced on this template.
*	Compilation of gettext mo files before distribution, when needed.
- To generate a gettext pot file, please run scons pot. A **addon-name.pot** file will be created with all gettext messages for your add-on. You need to check the buildVars.i18nSources variable to comply with your requirements.
*	Automatic generation of manifest localization files directly from gettext po files. Please make sure buildVars.py is included in i18nFiles.
*	Automatic generation of HTML documents from markdown (.md) files, to manage documentation in different languages.
* Automatic basic integration with AppVeyor, with automatic deployment to github releases when you push a tag.
* Generation of the basic template your addon will need, including the skeliton boilerplate code NVDA interfaces with.

(See the readme in your addon after you run the wizard for more information).

## Requirements

- a Python distribution (2.7 or greater is recommended). Check the [Python Website](http://www.python.org) for Windows Installers.

All software required is automagically installed when you install the add-on template from pip. In case you can't get it from pip, you need to do this manually.

- Scons - [Website](http://www.scons.org/) - version 2.1.0 or greater. Install it using **easy_install** or grab an windows installer from the website.
- Markdown-2.0.1 or greater, if you want to convert documentation files to HTML documents. You can [Download Markdown-2.0.1 installer for Windows](https://pypi.python.org/pypi/Markdown/2.0.1) or get it using `easy_install markdown`.
- cookie Cutter: This dependency automatically generates your add-on skeleton from parameters you provide to it. Install instructions: https://cookiecutter.readthedocs.io/en/latest/installation.html Or: ` $ pip install cookiecutter `

Things that are currently included as experimental. Note that the executables for these might be removed in a future version, requiring you to manually obtain them.

- GNU Gettext tools, if you want to have localization support for your add-on - Recommended. Any Linux distro or cygwin have those installed. You can find windows builds [here](http://gnuwin32.sourceforge.net/downlinks/gettext.php). Note that this template automatically places these inside your addon when you walk through the setup wizard. -->

## Usage

### To create a new NVDA add-on, taking advantage of this template: ###

- open a command prompt, or python capable shell (Unix shells should work as well).
- type `pip install NVDA-addonTemplate`
- Once installed, cd to the directory you want your add-on in.
- Then, simply type `NVDAAddonTemplate`
- when prompted, answer the following questions by typing on the command line. The system will except no input as the default, and may yell at you if you answer some prompts invalidly.
    - authorName (Defaults to John Doe): Put the name of the authors, separated by commas here.
    - authorEmail (Defaults to John.Doe225830@blacklist.com): Place the authors emails here, separated by commas.
    - projectName (Defaults to "Simple Addon"): Place the project's name here, (Usually you'll put what you want the addon to be called, but if it's an addon with many components, this might be different.
    - addonName (Defaults to "simpleAddon"): The name (Internal identifyer) that NVDA uses to recognize this addon. This should be a valid python module name.
    - addonSummary (Defaults to "Simple Addon"): This is the summary, or what your users will get to know for your addon. Something like "Indentone, musical indents" or "Tip of the Day" are good names.
    - addonDescription (Defaults to "This is my first add-on. It currently does nothing."): This is the description your add-on shows when you press about. If you want a multiline description, go to buildVars.py and do that there.
    - version (Defaults to "0.1.0-dev"): This is the version string you want your add-on to take on. Update this in buildVars.py whenever you release a new version.
    - addonURL (Defaults to None): Leave this as default if your add-on has no url, or put a url here to tell NVDA the url for this addon.
    - createGlobalPlugin (Yes/no) (Defaults to yes): Enter y or yes if you want the template to generate a globalPlugin, or n  if not. 
    - createAppModule (Yes/no) (Defaults to yes): Enter y if you want the template to generate an appModule, or Type n otherwise.
    - useContinuousIntegrationWithTravisCI (Yes/no) (Defaults to no): Enter y if you want the template to generate the necessary tools to use with travis CI, (A continuous integration system for windows) , or leave this as n if not.
    - If you said "y" to creating an app Module, you will be asked for the executable name. Enter the executable name for your appModule with no .exe.
The add-on will be placed in your current directory with underscore characters replacing space characters in the directory name.

## Todo;

Generate a template for speech Synthesiser and braille display drivers. Priority is lower because the average joe won't be writing one of these.