import time
import csv
import datetime
import smtplib
import config

def send_email(subject,msg):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS,config.PASSWORD)
		message='Subject: {}\n\n{}'.format(subject,msg)
		server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS,message)
		server.quit()
		print("Email successfully sent")
	except Exception as e:
		print("Email failed to send")
		print(e)

subject="Test subject"
msg="Hello suhas"

send_email(subject,msg)

now = time.strftime('%d-%m-%Y %H:%M:%S')
input_video1 = "./try/cropped6.mp4"
count1=29
inc=2
print(now)
row = [inc,now,input_video1,count1]

with open('vehicle_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()