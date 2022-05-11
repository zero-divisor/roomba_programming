Roomba Programming
========
Code and documentation to control roomba 600 Series with a Raspberry Pi.

## General Guides and Documentation
Guides for hardware setup:  
https://www.servomagazine.com/magazine/article/irobot-create2-raspberry-pi-picreate  
https://yakinikuman.github.io/pistreaming_roomba/

General Raspberry Pi documentation:  
https://www.raspberrypi.com/documentation/computers/os.html

Documentation for setting up a headless Rapberry Pi:  
https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi

Remote access with ssh:  
https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh

Copying files to the Raspberry Pi with scp:  
https://www.raspberrypi.com/documentation/computers/remote-access.html#using-secure-copy

## Required Python Libraries
Some of the Python files require additional libraries.  
You can install them with: pip install <library_name>

* manual_driving.py requires sshkeyboard
* irobot_create.py requires pyserial
