ExpressVPN for Kodi
==========
This script addon allows you to control ExpressVPN from within Kodi on Linux.

**Please note:** This will only work with the [ExpressVPN](http://www.expressvpn.com) service. If you have another VPN provider, I recommend using [OpenVPN for Kodi](http://brianhornsby.com/kodi_addons/openvpn). 

Currently this addon will only work with the **Linux version** as their Windows app doesn't allow parameters to be passed in (not sure about OSX/Android/iOS). If ExpressVPN update their apps, let me know and I will too.

Features
-----
- Start and stop ExpressVPN from with Kodi.
- Save your favourite servers in settings.
- Can be called directly using Kodi remote apps such as Yatse

Installation
------
1. Download the Linux ExpressVPN app from [here](https://www.expressvpn.com/vpn-software/vpn-linux).
2. Ensure it has been activated (see instructions on their website).
3. Download the latest zip file and install the addon. See [these instructions](http://kodi.wiki/view/HOW-TO:Install_an_Add-on_from_a_zip_file) for more details on installing addons from zip file.

Usage
------
There are two ways to use ExpressVPN for Kodi:

- **Via the graphical user interface in Kodi**

  1. Select Addons
  2. Select Programs
  3. Click on ExpressVPN
  4. If you have only one server configured in the settings dialog, it will connect automatically. Otherwise it will prompt you.
  5. To disconnect, open ExpressVPN (steps i-iii above) and it will ask you if you would like to disconnect. It will also tell you what server you are currently connected to.

- **Directly via the API (using a Kodi remote such as Yatse or a Kodi addon that will execute commands such as Commands)**

  1. To launch, execute: RunScript(script.expressvpn)
  2. If you want to pass in a parameter ot two, execute: RunScript(script.expressvpn,parameter,parameter2) i.e. RunScript(script.expressvpn,connect,usny)

  **Command-line options:**

  expressvpn [ connect | disconnect | status | list ] [ server ]

  expressvpn connect  
  expressvpn connect usny  
  expressvpn connect \"US - Chicago\"  
  expressvpn disconnect  
  expressvnp status  
  expressvpn list  

Settings
--------

Default Server: The server it will connect to unless you supply a parameter or have additional servers listed. By default it uses "smart", which is the closest server to you, geographically.

Additional servers: List the additional servers you would like to be prompted to connect to, separated by commas. As some of the full server names use commas, use the short name/alias (i.e. usny,usch,usmi)

License
------
ExpressVPN for Kodi is licensed under the [GPL 3.0 license](http://www.gnu.org/licenses/gpl-3.0.html).

Acknowledgements
------
Thank you to [Brian Hornsby](http://www.brianhornsby.com) whose addon [OpenVPN for Kodi](http://brianhornsby.com/kodi_addons/openvpn) was not only great to use (Until I switched to ExpressVPN and couldn't get OpenVPN to connect to it) but also provided a great reference to build this addon off of.