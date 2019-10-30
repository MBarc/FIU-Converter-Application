"""
This class is to distribute information amongst scripts who depend on it.

Author: Michael Barcelo
"""
import smtplib

def email(handler, message):
    #Sends emails
    server = smtplib.SMTP('smtpout.fiu.edu', 25) #establishing server

    server.connect('smtpout.fiu.edu', 25) # connecting to server
    
    server.sendmail(
      handler, # from address
      handler, # to address
      message) #message

    server.quit() # deallocating system resources'

def logger(message):
    #Logs error messages
    error_log = open("ERROR.txt", 'w')
    error_log.write(message)
    error_log.close()


try:
    
    with open("readme.txt") as info:
        for i, line in enumerate(info):

            if i == 0: #line 1
                if line.startswith("handler:"):
                    handler = line[8:]
                else:
                    raise Exception("[readme.txt Format Error]: The first 8 characters of line 1 should be 'handler:'.")

            elif i == 1: #line 2
                if line.startswith("file_path:"):
                    file_path = line[10:]
                else:
                    raise Exception("[readme.txt Format Error]: The first 10 characters of line 2 should be 'file_path:'.")

            elif i == 2: #line 3
                if line.startswith("feed_name:"):
                    feed = line[10:]
                else:
                    raise Exception("[readme.txt Format Error]: The first 10 characters of line 3 should be 'feed_name:'.")

            elif i == 3: #line 4
                if line.startswith("share_with:"):
                    share_with = line[11:]
                else:
                    raise Exception("[readme.txt Format Error]: The first 11 characters of line 4 should be 'share_with:'.")

except Exception as e:
    e = str(e)
    file_missing_error = "[Errno 2] No such file or directory: 'readme.txt'"    

    if e == file_missing_error: #if readme.txt is not within scope of information.py
        logger("[Info.txt Directory error] 'readme.txt' is not within the same directory. This error log was created because the program did not know who to email.")
    else: #email the error if it's not a 'readme.txt Directory Error'
        try:
            email(handler, e)
        except Exception as e: # If the email is unable to send
            e = str(e)
            if "User Unknown" in e:
                logger("[Info.txt Nonvalid Email Error]: Handler is not a valid email address. This error log was created because the program did not know who to email.")
            elif "Domain of sender address does not exist" in e:
                logger("[Info.txt Nonvalid Email Error]: Email is correctly written but the domain is not a proper '@fiu.edu' email.")
