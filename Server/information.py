'''
This script will hold information for other scripts that depend on it
'''

import os
import collections

from converter import complete_path

extensions = collections.defaultdict(int)

for path, dirs, files in os.walk(complete_path):
   for filename in files:
       extensions[os.path.splitext(filename)[1].lower()] += 1

extensions = []
extensions_count = []
for key,value in extensions.items():
    extensions.append(key)
    extensions_count.append(value)
