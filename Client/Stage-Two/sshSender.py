'''
This file is responsible for sending information to the Converting Server
'''
import os
import time
import config #same directory 

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
info.write(handler)
info.write(edited_path)
info.write(feed)
info.write(share_with)
info.write(scheme)
info.close()

#preps file_path for ssh usage

count = os.getcwd().count('\\')        
file_path = os.getcwd().replace('\\','/', count)

info_location = file_path + "/" + filename

#copies the file to the Converting Server
try:
    os.system('scp "%s" %s@%s:/haivisionconverterapp' % (info_location, handler, server_address))
    print('scp "%s" %s@%s:/haivisionconverterapp' % (info_location, handler, server_address))
    print("Connecting to server. . .")
    time.sleep(5)
except Exception as e: #if not able to copy the file
    if "Connection timed out" in e:
        logger("[Error SSHSender]: User is not on VPN")
    else:
        logger("[Error SSHSender]: " + e + " NOTE: Please email your Haivision System Administrator this error.")
