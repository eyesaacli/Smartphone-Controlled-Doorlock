import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pwm=GPIO.PWM(8,50)
pwm.start(0)

def SetAngle(angle):
        duty = angle / 18 + 2.5 // calculating duty cycle
		// which is a percentage measuring the amount of time
        GPIO.output(8, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(8, False)
        pwm.ChangeDutyCycle(0)

SetAngle(90)
sleep(2)
