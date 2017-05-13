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

import resources.lib.expressvpn as expressvpn
import resources.lib.settings as settings
import resources.lib.utils as utils
import sys

_expressvpn = expressvpn.ExpressVPN()
_settings = settings.Settings()
_utils = utils.Utils()

if (__name__ == "__main__"):

	parameterCount = _utils.getArgC()
	
	# Usage: expressvpn or expressvpn connect or expressvpn connect server
	if parameterCount == 1 or ((parameterCount == 2 or parameterCount == 3) and _utils.getArgV(1) == "connect"):
		
		# If already connected, ask user if they want to disconnect (also show current server)
		if _expressvpn.isConnected():
			disconnect = _utils.showYesNo(_utils.getString(32101), _utils.getString(32102) % _expressvpn.currentServer(), "", _utils.getString(32103), _utils.getString(32104), _utils.getString(32105))

			# If user wants to disconect, disconnect
			if (disconnect):
				disconnected = _expressvpn.disconnect()

				# If disconnection is successful, notify user
				if (disconnected):
					_utils.showNotification(_utils.getString(32106))
				else:
					_utils.showNotification(_utils.getString(32107))

				sys.exit()
			else:
				sys.exit()

		# Usage: expressvpn connect [server]
		if (parameterCount == 3):
			server = _utils.getArgV(2)

		# Haven't specified a server so work out which one to use
		else:
			defaultServer = _settings["default"]

			# If default is the only server available then use it
			if _settings["additional"] == "":
				server = defaultServer

			# Otherwise build list and prompt user
			else:
				serverList = _settings["additional"].split(",")
				serverList = map(lambda x: x.strip(), serverList)
				serverList.insert(0, defaultServer)

				serverIndex = _utils.showSelect("Select Server", serverList)
				
				# Has user tried to cancel out of the select box? If so, exit
				if (serverIndex == -1):
					sys.exit()

				# Use server that user selected
				server = serverList[serverIndex]

		# Try connecting
		_utils.showNotification(_utils.getString(32108))
		connected = _expressvpn.connect(server)
		
		# Notify user is successful or not
		if connected:
			_utils.showNotification(_utils.getString(32109) % server)
		else:
			_utils.showNotification(_utils.getString(32110), False)

	# expressvpn disconnect, expressvpn status, expressvpn list etc... 
	elif parameterCount == 2:
		if _utils.getArgV(1) == "disconnect":
		
			# If not connected, tell user there is nothing to do and exit
			if not _expressvpn.isConnected():
				_utils.showNotification(_utils.getString(21111))
				sys.exit()
			
			# Try and disconnect
			_utils.showNotification(_utils.getString(32112))
			disconnected = _expressvpn.disconnect()

			# Notify user if successful or not
			if disconnected:
				_utils.showNotification(_utils.getString(32106))
			else:
				_utils.showNotification(_utils.getString(32107), False)

		# Show user which server they are connected to
		elif _utils.getArgV(1) == "status":
			_utils.showNotification(_expressvpn.status())
		
		# Show user a list of available servers
		elif _utils.getArgV(1) == "list": 
			_utils.showTextviewer(_expressvpn.serverList())

		# Invalid command so show usage
		else:
			_expressvpn.showUsage()

	# Invalid command so show usage
	else:
		_expressvpn.showUsage()