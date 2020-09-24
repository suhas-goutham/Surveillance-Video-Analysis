# Imports
import tensorflow as tf
import cv2
import time
import csv
# Object detection imports
from utils import backbone
from api import object_counting_api
# Sending email imports
import time
import csv
import datetime
import smtplib
import config


road="Mantri Mall"
input_video1 = "./people/abcd2.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')


vcap = cv2.VideoCapture("./people/abcd2.mp4") 

if vcap.isOpened(): 
    # get vcap property 
    width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float
    height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = vcap.get(cv2.CAP_PROP_FPS)

print(fps)
print(width)
print(height)

is_color_recognition_enabled = 0 
roi = 600# roi line position
deviation = 4# the constant that represents the object counting area
output_video='./output_videos/app_output/people/output3.avi'
count1=object_counting_api.cumulative_object_counting_x_axis(output_video,input_video1, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation)

time1=time.strftime('%d-%m-%Y %H:%M:%S')

row = [time1,road,"Entrance 1",count1]
with open('people_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

#####################################################################################

input_video2 = "./people/people_walking_sh.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')


vcap = cv2.VideoCapture("./people/people_walking_sh.mp4") 

if vcap.isOpened(): 
    # get vcap property 
    width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float
    height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = vcap.get(cv2.CAP_PROP_FPS)

print(fps)
print(width)
print(height)

is_color_recognition_enabled = 0 
roi = 385 # roi line position
deviation = 1 # the constant that represents the object counting area

output_video='./output_videos/app_output/people/output2.avi'
count2=object_counting_api.cumulative_object_counting_x_axis(output_video,input_video2, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation) 

time2=time.strftime('%d-%m-%Y %H:%M:%S')
row = [time2,road,"Entrance 2",count2]

with open('people_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

count={}
count[input_video1]=count1
count[input_video2]=count2

def get_key(val):
	for key,value in count.items():
		if value==val:
			return key
	return "no such key"		


count_ar=[count1,count2]

print("Total count")
print(count1+count2)

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

count=count1+count2
subject="Crowd Management report for "+road
msg1="Entrance 1 has "+str(count1)+" people. "
msg2="Entrance 2 has "+str(count2)+" people. "
msg3="Total number of people inside the mall "+time2+" is "+str(count)+" people."
msg=msg1+msg2+msg3

send_email(subject,msg)
