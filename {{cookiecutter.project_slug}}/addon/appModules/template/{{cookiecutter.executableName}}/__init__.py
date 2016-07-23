# {{cookiecutter.projectName}}: An addon for {{ cookiecutter.executableName }}
{% if cookiecutter.addonURL != "None" %}
#Copyright (C) {{ cookiecutter.copyrightYear }} {{ cookiecutter.authorName }} <{{ cookiecutter.addonURL }}>
{% else %}
#Copyright (C) {{ cookiecutter.copyrightYear }} {{ cookiecutter.authorName }}
{% endif %}
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""{{ cookiecutter.addonName }}:
An app module that extends {{ cookiecutter.executableName }}
"""

import addonHandler
import appModuleHandler
#We need to initialize translation and localization support:
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		pass 
		#If you don't need this function, please remove it.
		
	def event_NVDAObject_init(self):
		pass
	
	def __init__(self):
		super(appModule, self).__init__()
	
	__gestures = {
		#Fill me in please. If you don't need me, delete me.
	}
	
