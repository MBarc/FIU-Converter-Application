'''
Purpose: Get list of newly converted videos
Author: Michael Barcelo
'''
import os
from os import listdir
from os.path import isfile, join

from information import file_path
from information import scheme

video_formats = ['.3gp',
                 '.avi',
                 '.dv',
                 '.m2ts',
                 '.m4a',
                 '.m4v',
                 '.mod',
                 '.mov',
                 '.mp3',
                 '.mp4',
                 '.mpeg',
                 '.mpg',
                 '.mts',
                 '.mxf',
                 '.trec',
                 '.vob',
                 '.wma',
                 '.wmv']

new_names = []
for root, dirs, files in os.walk(file_path):
  for name in files:
    for extension in video_formats:
      if name.endswith(extension) or name.endswith(extension).upper():
        
        def last_splitter(intake):
          index = name.rfind(".")
          new_name = name[:index] + ".mp4"
          return new_name
        
        if scheme is None:
          
          new_name = last_splitter(name)
          
          new_names.append(new_name)
        
        else:
          
          new_name = last_splitter(scheme + name)
          
          new_names.append(new_name)

with open('filenames.txt', 'w') as new_name_list:
for name in new_names:
  new_name_list.write(name + "\n")
