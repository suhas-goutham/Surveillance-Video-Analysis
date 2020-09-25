import os
import time
import pandas as pd
import datetime
import videosplit
import Main
import cv2
from PIL import Image
import pymongo
import time
#import check_ocr

if __name__ == '__main__':
    name1 = str(input('Enter the name of the video: '))
    name = './input_videos/'+name1
    (vdolength,totalFrames) = videosplit.Launch(name)
	# The name of the folder to store the frames of the video
    os.chdir('data')

    result = {}
    result_imag = {}
    #startTime = datetime.now()
    startTime = time.time()
    for f in os.listdir():
        pred, img = Main.main(f)
        if pred in result.keys():
            result[pred] = result[pred] + 1
        elif pred != ' ':
            result[pred] = 1
            result_imag[pred] = img

    #endTime = datetime.now()
    endTime = time.time()
    print(result)

    a=list(result.keys())

    '''
    listOfPossiblePlates=result.keys()

    listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
    plate = listOfPossiblePlates[0]
    img = result_imag[plate]
    '''
    # Sort the list of number plates by the frequency of their occurance
    l = {x: y for y, x in result.items()}
    r = list(sorted(l.keys()))
    print(r)

    index = r[len(r) - 1]
    plate = l[index]
    img = result_imag[plate]
    executionTime = "{0:.2f}".format(endTime - startTime)
    #for plate in result:

    print('The name plate is :', plate) #, ' frequency is: ', result[plate])
    try:
        Image.fromarray(img).show()
    except:
        print("Problem in displaying license plate")
    #print('execution time is : ' + executionTime)
    
    #################################
    #Data is stored in CSV file
    raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
        'v_number': [plate]}

    df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
    df.to_csv('data.csv')
    #################################
    os.chdir('..')
    #licensePlatePath = name.split('.')[0]+'.jpg'
    licensePlatePath = './licensePlatePath/' + name1.split('.')[0]+'.jpg'
    try:
        cv2.imwrite(licensePlatePath,img)
    except:
        print("Problem in writing license plate image")
    cv2.imshow("final image",img)
    
    name2=name1.split('.')[0]+'.jpg'
    os.system("python check_ocr.py "+name2)
    #check_ocr.find_ocr(img)
    # If u want to see the freqiencies for predictions then uncomment the below 2 lines.
    """
    for i in result.keys():
        print(i, ' : ', result[i])
    """