## Stage 1:
        -Generates readme.txt that the user can fill out.
        
## Stage 2:
        -Interprets user input from readme.txt and sends it, via SSH, to the Linux Server.
        -Linux server uses this information to go through the converting process.
        -Once the Linux server is done, it will send an email to the handler to notify them that they can start Stage 3.
        
## Stage 3:
        -Interprets user input from readme.txt in order to add videos to a feed and share them with the appropriate group.



For each stage, one .py file must be converted into .exe. Those specific .py files are listed below.\
        **Stage 1:** readme.py\
        **Stage 2:** sshSender.py\
        **Stage 3:**
       
***Note: Make sure to fill out the config.py before you create any .exe files!***
        
##The files can be converted to .exe using Pyinstaller.
                
                C:\Users\username> pip install pyinstaller
                C:\Users\username> cd path/to/py/file/you/want/to/convert
                C:\Users\username> pyinstaller -F nameOfPyFile.py 
                
