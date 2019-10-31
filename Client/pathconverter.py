'''
This script with convert the user's input from Windows format to Linux format. 
This is the prep the information for the Linux server.
'''
from information import file_path

alphabet = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H','I', \
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letter in alphabet:
            #If file path starts with a letter (either uppercase or lowercase). . . 
            if file_path.startswith(letter + ':') or file_path.startswith(letter.lower() + ":"):
                        file_path = file_path[2:]
                        count = file_path.count('\\')
                        file_path = file_path.replace('\\','/', count) # Ready for Linux server
