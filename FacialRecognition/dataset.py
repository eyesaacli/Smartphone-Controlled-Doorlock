import cv2
import os
cam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id  and press <return> ==> ') # prompting user for id
print("\n [INFO] Initializing face capture. Look at the camera and wait ...")

# Initialize individual sampling face count
count = 0
while (True):
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
		count += 1
		
		# Save the captured image in the datasets folder
		cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
		cv2.imshow('image', img)
	k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
	if k == 27:
		break
	elif count>=30:
		break

# Notify user of program termination
print("\n [INFO] Exiting Program");
cam.release()
cv2.destroyAllWindows()
