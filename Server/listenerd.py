'''
This is a daemon that will detect when new information gets shared with the Linux server.
Runs once an hour.

Note: Assumes a new info.txt will appear within every 7 years.
'''
import os
import subprocess
import time
from daemon import runner
import psutil #to check PID names
import os, time, datetime, calendar
from datetime import date

class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.sterr_path = '/dev/tty'
		self.pidfile_path = '/tmp/your-pid-name.pid'
		self.pidfile_timeout = 5

	def run(self):

		try:
			while True:

				info = os.getcwd() + "/info.txt"

				try:
					if os.path.exists(info):
						
						'''Creation information for info.txt'''
						creation_time = time.ctime(os.path.getctime(info)) #parse data from this
						day = creation_time[:-21]
						hour = int(creation_time[11:-11])
						month = str(creation_time[4:7])
						
						'''Time information when this script is executed'''
						current_day = calendar.day_name[date.today().weekday()] #parse data from this
						current_day_initial = current_day[:-6]
						current_hour = datetime.datetime.now().hour

						month_number = datetime.datetime.now().month #returns the int of the month

						#determining what month it is by the given number
						if month_number == 1:
							current_month = "Jan"
						elif month_number == 2:
							current_month = "Feb"
						elif month_number == 3:
							current_month = "Mar"
						elif month_number == 4:
							current_month = "Apr"
						elif month_number == 5:	
							current_month = "May"
						elif month_number == 6:
							current_month = "Jun"
						elif month_number == 7:
							current_month = "Jul"
						elif month_number == 8:
							current_month = "Aug"
						elif month_number == 9:
							current_month == "Sep"
						elif month_number == 10:
							current_month = "Oct"
						elif month_number == 11:
							current_month = "Nov"
						elif month_number == 12:
							current_month = "Dec"
						
						#If info.txt is less than 1 hour old, then start converter.py
						if hour == current_hour and day == current_day_initial and month == current_month:
							
							pids = [pid for pid in os.listdir('/proc') if pid.isdigit()] #gets a list of all pids in /proc

							tracker = [] #keeps track of pids with ffmpeg
							for pid in pids:
								process_name = psutil.Process(pid) # returns the name of the pid

								if "ffmpeg" in process_name:
									tracker.append(process_name)

							if len(tracker = 0): #if there's not a process with ffmpeg as a substring ; if tracker is empty
								os.system("python3 /haivisionconverterapp/converter.py") #command to start converter.py
							else:
								pass
						else:
							pass
				except Exception as e:
					raise

				time.sleep(60 * 60) #every hour
		
		except Exception as e:
			raise

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
