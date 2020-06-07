# Infinity

This is a tool to help with exfilitration in red/blue team exercises by automating the steps required to access a free hour of wifi usage from certain wifi hotspots.

Changing the MAC address is only required if the system you are accessing has already used its free wifi session.

Tested with 

* Ubuntu 20.04
* Firefox 77.0.1 (64-bit)
* Geckodriver 0.26.0
* Selenium 3.141.0
* GNU MAC changer 1.7.0

## DISCLAIMER

THIS TOOL IS BEING PROVIDED FOR EDUCATIONAL PURPOSES WITH THE INTENT FOR RESEARCH. 

## USAGE

```
Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from infinity import Infinity
>>> from infinity import User
>>> u = User()
>>> i = Infinity("wlp2s0")
>>> i.set_wifi_state(enabled=False)
>>> i.randomize_mac()
Current MAC:   f5:fb:02:b9:37:4c (unknown)
Permanent MAC: cd:18:65:2c:81:47 (unknown)
New MAC:       ba:2d:44:3e:54:a0 (unknown)
>>> i.set_wifi_state(enabled=True)
>>> i.handle_portal(u)
>>>
```