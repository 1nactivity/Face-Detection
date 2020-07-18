import cv2
import serial, time, numpy, winsound, sys
from subprocess import call


call('color 2', shell=True)

#haarcascade for facial detection
faceCascade = cv2.CascadeClassifier('utils/frontface.xml')
frameWidth = 640
frameHeight = 480


#menu
print(" Select an option:")
print(" {1}--On")
print(" {2}--Off")
x = int(input(" User:"))



if x == 2:
    winsound.Beep(500,500)
    winsound.Beep(1000,500)
    winsound.PlaySound("utils/sleep", winsound.SND_FILENAME)
    sys.exit()

elif x == 1:
    print("STARTING...")
    winsound.Beep(1000,500)
    winsound.Beep(500,500)
    winsound.PlaySound("utils/sentry", winsound.SND_FILENAME)
    time.sleep(1.2)
    print("STARTED")
    winsound.PlaySound("utils/canvas", winsound.SND_FILENAME)
    winsound.PlaySound("utils/second", winsound.SND_FILENAME)
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, frameWidth)
    video_capture.set(4, frameHeight)
    video_capture.set(10,150)
    

    while True:
        
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces1 = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20)
        )
        
        

        #face square 
        #software view doesn't work(bug)
        for (x, y, w, h) in faces1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            print("located")
            winsound.PlaySound("utils/beep", winsound.SND_FILENAME)
            winsound.PlaySound("utils/first", winsound.SND_FILENAME)
            
    
          


  


