# create the application object
from flask import Flask, request
import sys
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
	option= request.form['option']
	print ("option is "+option,file=sys.stdout)

	if option=="1a":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python vehicle_counting1.py 1")
	elif option=="1b":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python vehicle_counting2.py 2")
	elif option=="1c":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python vehicle_counting3.py 3")
	elif option=="2a":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python people_counting1.py 4")
	elif option=="2b":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python people_counting2.py 5")
	elif option=="2c":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api")
		os.system("python people_counting3.py 6")
	elif option=="3":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/number_plate/ALPR/Main Program")
		os.system("python Start.py 7")
	elif option=="4a":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api/checking")
		os.system("python check2.py 4a")
	elif option=="4b":
		os.chdir("C:/Users/Priya/Desktop/8th sem/Project/tensorflow_object_counting_api/checking")
		os.system("python check2.py 4b")
	else:
		print("You have entered a wrong option")
	return 'OK.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)