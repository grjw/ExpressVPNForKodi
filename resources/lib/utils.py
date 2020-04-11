# This file is part of ExpressVPN For Kodi.

#     ExpressVPN For Kodi is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     ExpressVPN For Kodi is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with ExpressVPN For Kodi.  If not, see <http://www.gnu.org/licenses/>.

import sys
import xbmc
import xbmcaddon
import xbmcgui

class Utils:
	def __init__(self):
		self.addon = xbmcaddon.Addon()
		self.addonName  = self.addon.getAddonInfo("name")
		self.addonPath = self.addon.getAddonInfo("path")
		self.iconPath = xbmc.translatePath("%s/%s" % (self.addonPath, "resources/icon.png"))
		self.failedIconPath = "DefaultIconError.png"

	def getArgC(self):
		return len(sys.argv)

	def getArgV(self, index):
		return sys.argv[index]

	def getString(self, id):
		return self.addon.getLocalizedString(id)

	def showTextviewer(self, text):
		xbmcgui.Dialog().textviewer(self.addonName, text)

	def showOK(self, heading, line1, line2 = "" , line3 = ""):
		xbmcgui.Dialog().ok(heading, line1, line2, line3)

	def showYesNo(self, heading, line1, line2 = "", line3 = "", nolabel = "No", yeslabel = "Yes"):
		return xbmcgui.Dialog().yesno(heading, line1, line2, line3, nolabel, yeslabel) == 1

	def showSelect(self, heading, list):
		return xbmcgui.Dialog().select(heading, list)

	def showNotification(self, text, success = True):
		if success:
			image = self.iconPath
		else:
			image = self.failedIconPath
			
		command = 'Notification(%s, %s, %s, %s)' % (self.addonName, text, 5000, image)
		xbmc.executebuiltin(command)