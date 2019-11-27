'''
This file will run publishFeed.py and shareVideos.py concurently.
'''

import subprocess

subprocess.run("python3 publishFeed.py & python3 shareVideos.py, shell = True)
