'''
This script will send the report back to the handler's email
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from converter import handler #to know where to send the email to/from
from converter import file_path #for email_body
import datetime #for email body

import config #same directory


date = datetime.datetime.today()
date = date.month + "/" + date.day + "/" + date.year

file_path = r"%s" % file_path #converts string to raw string format ; for email body

#Setup the MIME
message = MIMEMultipart()
message['From'] = handler
message['To'] = handler
message['Subject'] = 'Conversion Report %s' % date

email_body = '''
This email was sent to signal that the conversion process for %s has completed.
Attached to this email is a detailed report containing information about the conversion process.
You may start Stage 3.

If you are encountering errors with the conversion process, please let your Haivision Systems Administrator know.

Thank You.
''' % file_path

attach_file_name = 'report.xlsx' #name of report excel file

#Putting together the email
message.attach(MIMEText(email_body, 'plain')) #attaching the email body

#Attaching then encoding the attachment
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream') #Opens up to stream to attach file to
payload.set_payload((attach_file).read()) #sets the file as the payload
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload) #Actually attaches the payload to the email

#Create SMTP session for sending the mail
session = smtplib.SMTP(config.smtp['ip'], config.smtp['port'])
session.connect(config.smtp['ip'], config.smtp['port']) # Connects to server
session.starttls() #enables security
text = message.as_string()
session.sendmail(handler, handler, text) #Sends email ; sendmail(sender, receiver, message)
session.quit()
