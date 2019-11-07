'''
This file is responsible for sending information to the Converting Server
'''
import os
import time
import config #same directory
import subprocess

from information import logger

from pathconverter import file_path as edited_path
from information import handler
from information import feed
from information import share_with
from information import scheme

server_address = config.server['ip'] #this ip address should be the server that is handling the actual conversion

filename = 'info.txt' # this variable should be the name of file that will be sent over SSH 

#creating the file to ssh to the Converting Server
info = open(filename, 'w')
print(filename, "has been created! Populating now. . .")
info.write(handler)
print("Appended handler.")
info.write(edited_path)
print("Appended file path.")
info.write(feed)
print("Appended feed.")
info.write(share_with)
print("Appended group.")
info.write(scheme)
print("Appended scheme.")
info.close()

print("Finished appending information! Continuing. . .")
time.sleep(3)
#preps file_path for ssh usage

count = os.getcwd().count('\\')

file_path = os.getcwd().replace('\\','/', count)

info_location = file_path + "/" + filename


#copies the file to the Converting Server
try:

    def username(variable,split_from):
        '''grabs username from email '''
        index = variable.rfind(split_from)
        new_variable = variable[:index]
        return new_variable

    username = username(handler, "@")
    command = 'scp "%s" %s@%s:/haivisionconverterapp' % (info_location, username, server_address)
    print("Sending information to %s. You may be prompted to enter your password for %s." % (server_address, server_address))
    test = subprocess.call(command, shell=True) #transfers file to server

    if test == 1: #enters if statement if user is not on VPN
        error = "[Error SSHSender]: User is not on VPN"
        print(error)
        logger(error)
        time.sleep(2)
        print("Exiting now. . .")
        time.sleep(5)
    
except Exception as e: #if not able to copy the file
    logger("[Error SSHSender]: " + e + " NOTE: Please email your Haivision System Administrator this error.")
