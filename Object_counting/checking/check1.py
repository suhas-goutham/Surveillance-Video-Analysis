import os
import mimetypes
from email.mime.multipart import MIMEMultipart

print("Choose the operation you want to perform")

print("Press 1 for traffic monitoring")
print("Press 2 for crowd management")
print("Press 3 for license plate detection")
print("Press 4 for daily reports of traffic management")

option=int(input())

if option==1:
	os.system("python vehicle_counting.py 1")
elif option==2:
	os.system("python people_counting.py 2")
elif option==3:
	os.system("python C:/Users/Priya/Desktop/8th sem/Project/number_plate/ALPR/Main Program/Start.py 3")
elif option==4:
	os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api/checking")
	os.system("python check3.py 4")
else:
	print("You have entered a wrong option")

print("Done running")