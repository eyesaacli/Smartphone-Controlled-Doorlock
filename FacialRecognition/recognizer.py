import cv2
import numpy as np
import os 
import RPi.GPIO as GPIO
from time import sleep

#setting up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pwm = GPIO.PWM(8,50)
pwm.start(0)

servo = False # variable to check if lock has been turned

# function that calculates duty cycle and moves servo
def SetAngle(angle):
	duty = angle / 18 + 2.5
	GPIO.output(8,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(8,False)
	pwm.ChangeDutyCycle(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# array to names corresponding to id of faces
names = ['Isaac', 'Unknown', 'Unkown', 'Unknown', 'Unknown', 'Unknown'] 

cam = cv2.VideoCapture(0)

while True:
	# variable to check what key is pressed
	k = cv2.waitKey(10) & 0xff 
	ret, img =cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
	)
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
		# checking confidence to see if face is recognized
		if (confidence < 60):
			id = names[id]
			if(k == 32): # if 'SPACE' is pressed
				if(servo == False):
					SetAngle(90)
					servo = Tru
				elif(servo == True):
					SetAngle(0)
					servo = False
		else:
			id = "Unknown" 
			cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
	cv2.imshow('camera',img)
	if k == 27: # if 'ESC' has been pressed
		break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleaning up stuff")
pwm.stop()
GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()
