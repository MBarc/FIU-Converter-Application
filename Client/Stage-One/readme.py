'''
This file is to genreate 'README.txt'
'''


readme = open("readme.txt", 'w+')

readme.write("handler:\n")
readme.write("file_path:\n")
readme.write("feed_name:\n")
readme.write("share_with:\n")
readme.write("scheme:\n")

readme.write('\n\n\n')

readme.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
readme.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*ReadMe-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
readme.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
readme.write('\n')
readme.write('The user needs to fill out the above prompts with the correct information.\n')
readme.write('\n')
readme.write('Examples\n')
readme.write('-------\n')
readme.write('Note: For the examples, there are no spaces between the colon and information inputed by the user\n')
readme.write('\n')
readme.write('Handler is the recepient of emails. There should be one 1 FIU-approved email listed.\n')
readme.write('\n')
readme.write("                    handler:mbarcelo@fiu.edu\n")
readme.write('\n')
readme.write('file_path is the location where the videos are being stored. This program assumes the path is in Windows format.\n')
readme.write('\n')
readme.write("                    file_path:Z:\ABC_ERICA_Practical\n")
readme.write('\n')
readme.write('feed_name is the name of the appropriate feed listed on the Haivision portal.\n')
readme.write('\n')
readme.write("                    feed_name:ABC Erica - Psych-Evaluations\n")
readme.write('\n')
readme.write('share_with is the appropriate group that the videos should be shared with.\n')
readme.write('\n')
readme.write("                    share_with:CCF_HMP_Psych-Evaluations_Members\n")
readme.write('\n')
readme.write('scheme is the naming convention that should go before the title of the videos.')
readme.write('\n')
readme.write('                    scheme:Naming_Convention_')


readme.close()
