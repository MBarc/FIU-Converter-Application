'''
This file is responsible for sending information to the Converting Server
'''
import os
import time

from information import email
from information import logger

from information import file_path
from information import handler
from information import feed
from information import share_with

from pathconverter import file_path as edited_path

server_address = 'xxx.xxx.xxx.xxx' #this ip address should be the server that is handling the actual conversion

filename = 'info.txt' # this variable should be the name of file that will be sent over SSH 

#creating the file to ssh to the Converting Server
info = open('info.txt', 'w')
info.write(handler)
info.write(edited_path)
info.write(feed)
info.write(share_with)
info.close()

#preps file_path for ssh usage

count = os.getcwd().count('\\')        
file_path = os.getcwd().replace('\\','/', count)

info_location = file_path + "/" + filename

#simply grabs username from provided email
username = handler[:8]

#copies the file to the Converting Server
try:
    os.system('scp "%s" %s@%s:/haivisionconverterapp' % (info_location, username, server_address))
    print('scp "%s" %s@%s:/haivisionconverte' % (info_location, username, server_address))
    time.sleep(5)
except Exception as e: #if not able to copy the file
    if "Connection timed out" in e:

        try:
            email(handler, '[sshSender Error]: User is not on VPN.')
        except Exception as e: # If the email is unable to send
            e = str(e)
            if "User Unknown" in e:
                logger("[sshSender Nonvalid Email Error]: Handler is not a valid email address. This error log was created because the program did not know who to email.")
            elif "Domain of sender address does not exist" in e:
                logger("[sshSender Nonvalid Email Error]: Email is correctly written but the domain is not a proper '@fiu.edu' email.")
