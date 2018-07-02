#Used this to test servo movement in initial stages of development
import RPi.GPIO as GPIO
from time import sleep

#Setting up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT) #setting pin #8 as output
pwm=GPIO.PWM(8,50) 
pwm.start(0)

def SetAngle(angle): #function that performs calculatiosn to set angle of servo
        duty = angle / 18 + 2.5 #calculating duty cycle which is a percentage 
	#measuring the amount of time that the signal is on
        GPIO.output(8, True)
        pwm.ChangeDutyCycle(duty) #actually changes the duty cycle and makes servo move
        sleep(1)
        GPIO.output(8, False)
        pwm.ChangeDutyCycle(0)

SetAngle(90) #calls the function to move the servo
sleep(2)
SetAngle(0) #calls the function to move servo back to initial position

pwm.stop()
GPIO.cleanup()
