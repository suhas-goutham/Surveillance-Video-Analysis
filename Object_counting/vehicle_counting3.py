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

road="Mekhri Circle"

input_video1 = "./try/cropped5.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')

vcap = cv2.VideoCapture('./try/cropped5.mp4') 

if vcap.isOpened(): 
    # get vcap property 
    width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float
    height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = vcap.get(cv2.CAP_PROP_FPS)

is_color_recognition_enabled = 0 
roi = 500 # roi line position
deviation = 5# the constant that represents the object counting area
output_video='./output_videos/app_output/vehicle/output1.avi'
count1=object_counting_api.cumulative_object_counting_y_axis(output_video,input_video1, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation) 

time1=time.strftime('%d-%m-%Y %H:%M:%S')
row = [time1,road,"Lane 1",count1]

with open('vehicle_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()
###################################################################

input_video2 = "./try/cropped7_sh.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')

vcap = cv2.VideoCapture('./try/cropped7_sh.mp4') 

if vcap.isOpened(): 
    # get vcap property 
    width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float
    height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = vcap.get(cv2.CAP_PROP_FPS)

is_color_recognition_enabled = 0 
roi = 500 # roi line position
deviation = 4# the constant that represents the object counting area
output_video='./output_videos/app_output/vehicle/output2.avi'
count2=object_counting_api.cumulative_object_counting_y_axis(output_video,input_video2, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation) 

time2=time.strftime('%d-%m-%Y %H:%M:%S')
row = [time2,road,"Lane 2",count2]
with open('vehicle_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()
#######################################################################

input_video3 = "./try/cropped9.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')

vcap = cv2.VideoCapture('./try/cropped9.mp4') 

if vcap.isOpened(): 
    # get vcap property 
    width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float
    height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
    fps = vcap.get(cv2.CAP_PROP_FPS)

is_color_recognition_enabled = 0 
roi = 500 # roi line position
deviation = 4# the constant that represents the object counting area
output_video='./output_videos/app_output/vehicle/output1.avi'
count3=object_counting_api.cumulative_object_counting_y_axis(output_video,input_video3, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation) 

time3=time.strftime('%d-%m-%Y %H:%M:%S')
row = [time3,road,"Lane 3",count3]

with open('vehicle_file.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

count={}
count['1']=count1
count['2']=count2
count['3']=count3

def get_key(val):
    for key,value in count.items():
        if value==val:
            return key
    return "no such key"        


count_ar=[count1,count2,count3]

print(count)
print(get_key(max(count_ar)))
print(max(count_ar))

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

subject="Traffic monitoring continuous report for "+road
msg1="Lane 1 has "+str(count1)+" vehicles at time "+str(time1)+". Lane 2 has "+str(count2)+" vehicles at time "+str(time2)+". Lane 3 has "+str(count3)+" vehicles at time "+str(time3)+"."
msg2="The largest number of vehicles is detected on lane "+str(get_key(max(count_ar)))+" with "+str(max(count_ar))+" vehicles"
msg=msg1+msg2

send_email(subject,msg)
