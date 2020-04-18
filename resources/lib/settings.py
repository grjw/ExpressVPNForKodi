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

import xbmcaddon

class Settings:
	def __init__(self):
		self.addon = xbmcaddon.Addon()

	def __getitem__(self, key):
		value = self.addon.getSetting(key)
		if value.isdigit():
			return int(value)
		else:
			return value

	def open(self):
		self.addon.openSettings()