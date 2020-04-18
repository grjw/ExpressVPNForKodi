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

import re
import subprocess
import utils

_utils = utils.Utils()

class ExpressVPN:

	def connect(self, server):
		return subprocess.call(["expressvpn", "connect", server]) == 0
	
	def disconnect(self):
		return subprocess.call(["expressvpn", "disconnect"]) == 0

	def status(self):
		return subprocess.check_output(["expressvpn", "status"])

	def isConnected(self):
		connected = False
		ret = re.search("Connected\ to\ (.+)", self.status())
		if ret is not None :
				connected = True
		return connected

	def currentServer(self):
		return re.search("Connected\ to\ (.+)", self.status()).group(1) 

	def serverList(self):
		return subprocess.check_output("expressvpn list | awk '{gsub(/[\\t]+/,\"\t\")}1' | awk 'BEGIN {FS=\"\\t\"}; {print $1 \" - \" $2}'", shell = True)

	def showUsage(self):
		_utils.showTextviewer("Usage: expressvpn [ connect | disconnect | status | list ] [ server ]\n\nexpressvpn connect\nexpressvpn connect usny\nexpressvpn connect \"US - Chicago\"\nexpressvpn disconnect\nexpressvnp status\nexpressvpn list")