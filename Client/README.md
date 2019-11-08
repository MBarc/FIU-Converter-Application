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
***Note: Please change the name of the .exe to reflect what stage it is. For example: readme.exe -> Stage-One.exe.***
        
## The files can be converted to .exe using Pyinstaller.
                
                C:\Users\username> pip install pyinstaller
                C:\Users\username> cd path/to/py/file/you/want/to/convert
                C:\Users\username> pyinstaller -F nameOfPyFile.py 
                
After all 3 .py files have been converted to .exe. Place them all into the same directory (perferably an empty directory).

### Walkthrough

**Step 1.)** Click on Stage-One.exe.\
**Step 2.)** Fill out information inside generated readme.txt.\
**Step 3.)** Click on Stage-Two.exe.\
**Step 4.)** Enter password.\
**Step 5.)** Wait until you receive an email from the Linux server that notifies you that the conversion process has completed.\
**Step 6.)** Click on Stage-Three.exe.\
**Step 7.)** Wait until process is completed.
