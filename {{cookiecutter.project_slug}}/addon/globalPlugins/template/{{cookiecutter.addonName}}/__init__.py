# {{cookiecutter.projectName}}: An Add-on for nvda that does <Insert thing here>
{% if cookiecutter.addonURL != "None" %}
#Copyright (C) {{ cookiecutter.copyrightYear }} {{ cookiecutter.authorName }} <{{ cookiecutter.addonURL }}>
{% else %}
#Copyright (C) {{ cookiecutter.copyrightYear }} {{ cookiecutter.authorName }}
{% endif %}
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""{{ cookiecutter.addonName }}:
A global plugin 
"""

import addonHandler
import globalPluginHandler
#We need to initialize translation and localization support:
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		pass 
		#If you don't need this function, please remove it.
		
	def __init__(self):
		super(GlobalPlugin, self).__init__()
	
	__gestures = {
		#Fill me in please. If you don't need me, delete me.
	}
	
