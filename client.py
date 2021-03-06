#!/usr/bin/python
#
# Copyright (c) 2018  Krishna Kotha <krkotha@cisco.com>
# All rights reserved.

# this is the script you need to executed to run on all the devices. It will get all the device details from the ip_address.py file and the command to be executed from the commands.py file

# import the requests library
import v2
import ip_address
import sys
import logging

#switch_name = raw_input('Please enter switch name: ')

for key in ip_address.switch_list:
    #creates a log file called output.log
    logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO)
    obj = v2.NetworkDevice()

    # creates the telnet connection (using console) for each device and stores the output to the result
    result = obj.telnetToSwitch(ip_address.switch_list.get(key))
    print result

    #logs the output to a output log file, when executing this script it re-erases the file everytime
    logging.info(result)

