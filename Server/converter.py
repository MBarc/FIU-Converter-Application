#!/usr/bin/env python3
'''
Purpose: Convert all video formats into .MP4 for CCF$, CCF2$, CCF3$

Author: Michael Barcelo
'''

import os 
from os import listdir
from os.path import isfile, join
import ffmpy #converting the videos 
from shutil import copyfile #for MP4 videos
import smtplib #for emails
import time #for measuring the duration of execution
import datetime #for recording start/end times of execution

duration_start = time.time()
start_time = datetime.datetime.now()

'''
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Step 1: Obtain information from info.txt
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
'''
def logger(message):
	#Logs error messages
	error_log = open("ERROR.txt", 'a')
	error_log.write(message)
	error_log.close()

#Defines drive_path
info = open("info.txt", "r")
for line in info:
	if "/" in line:
		drive_path = line #directory to start searching

mount_path = "/mnt" #where the CCF drives are mounted
depository = "/newvideos/" #where the converted videos will be deposited 

#establishing what drive the file path is in
if os.path.exists((mount_path + "/CCF" + drive_path).rstrip()):
	complete_path = (mount_path + "/CCF" + drive_path).rstrip()
elif os.path.exists((mount_path + "/CCF2" + drive_path).rstrip()):
	complete_path = (mount_path + "/CCF2" + drive_path).rstrip()
elif os.path.exists((mount_path + "/CCF3" + drive_path).rstrip()):
	complete_path = (mount_path + "/CCF3" + drive_path).rstrip()


try: #checks to see if complete_path got defined
	complete_path
except Exception as e: # if complete_path isn't defined
	logger("[Converter Error]: Given path does not exist within CCF, CCF2, or CCF3. \n" \
		"Path given:" + drive_path + "\n")

'''
*-*-*-*-*-*-*-*-*-*-*-*-*-*
Step 2: converting videos
*-*-*-*-*-*-*-*-*-*-*-*-*-*
'''
successful = [] #contains the videos that were successfully converted
failed = [] #contains the videos that were not successfully converted
not_attempted = [] #contains videos and/or files whose extensions are not handled
for root, dirs, files in os.walk(complete_path, topdown=False):
		
	for name in files:

		def splitter(variable,split_from, extension):
			'''Splits an extension's name starting from "split_from". '''
			index = variable.rfind(split_from)
			new_variable = variable[:index] + extension
			return new_variable		
					
		video_path = root + "/" + name
		video_destination = depository + splitter(name, ".", ".mp4")

		def empty_convert(video_input, video_output):
			'''Default command to convert videos'''
			ff = ffmpy.FFmpeg(inputs={'%s'%video_input: None}, outputs={'%s'%video_output: None})
			ff.run()

		def single_convert(video_input, video_output):
			'''Responsible for converting videos that only need to be converted once'''
			empty_convert(video_input, video_output)

		def double_convert(video_input, video_output):
			'''Responsible for converting videos that need to be converted twice'''
			second_conversion = splitter(video_destination, ".", ".mpeg")
			empty_convert(video_input, second_conversion)
			empty_convert(second_version, video_output)
			os.remove(second_conversion)

		def triple_convert(video_input, video_output):
			'''Responsible for converting videos that need to be converted three times'''
			second_conversion = splitter(video_destination, ".", ".avi")
			third_conversion = splitter(video_destination, ".", ".mpeg")
			empty_convert(video_input, second_conversion)
			empty_convert(second_conversion, third_conversion)
			empty_convert(third_conversion, video_output)
			os.remove(second_conversion)
			os.remove(third_conversion)

		try:
			if name.endswith((".MTS", ".MOV", ".m2ts", ".mod", ".m4v", ".3gp", ".trec", ".VOB", ".mpeg")):

				single_convert(video_path, video_destination)

			elif name.endswith(".avi"):
		
				double_convert(video_path, video_destination)

			elif name.endswith((".asf", ".mpg", ".mxf", ".dv")):
				
				triple_convert(video_path, video_destination)

			elif name.endswith(".mp4"): #no need for conversion, just copy the file to the destination

				copyfile(video_path, video_destination)

			elif name.endswith((".WMA", ".m4a", ".mp3")): #this is for audio files

				os.system("ffmpeg -y -loop 1 -r 6 -i black.jpg -i '%s' -shortest -c:v libx264 -preset ultrafast -tune stillimage -pix_fmt yuv422p -c:a aac -strict -2 '%s'" % (video_path, video_destination))
			else:
				not_attempted.append(name)

			successful.append(name)
		else Exception as e:
			logger(name, "was not able to be converted!\n")

			failed.append(name)

#Recording data relevant to extensions
every_file_extension = []
for root, dirs, files in os.walk(complete_path)
	for name in files:

		def extension_grabber(intake):
			'''returns the extension of a given file'''
			index = name.rfind(".")
			extension = name[index:]
			return extension
		
		every_file_extension.append(extension_grabber(name))
extensions = set(every_file_extension)


duration_end = time.time()
duration = str(end_time - start_time)
end_time = datetime.datetime.now()
