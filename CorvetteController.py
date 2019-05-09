import RPi.GPIO as GPIO
from time import sleep

class CorvetteController():
    
    GPIO.setmode(GPIO.BOARD)
##right left dc motor pins
    Motor1F = 16
    Motor1B = 18
    Motor1E = 22

##foward right dc motor pins
    Motor2F =19
    Motor2B = 21
    Motor2E = 23


    def forward(self):
        GPIO.output(Motor2F,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

    def reverse(self):
        GPIO.output(Motor2F,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

    def right(self):
        GPIO.output(Motor1F,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

    def left(self):
        GPIO.output(Motor1F,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

    def release(self):
        GPIO.output(Motor1E, GPIO.LOW)
        GPIO.output(Motor2E, GPIO.LOW)


car = CorvetteController()
car.forward()
