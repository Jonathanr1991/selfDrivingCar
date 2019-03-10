import RPi.GPIO as GPIO
from time import sleep

class CorvetteController():
##right left dc motor pins
    Motor1F = 16
    Motor1B = 18
    Motor1E = 22

##foward right dc motor pins
    Motor2F =19
    Motor2B = 21
    Motor2E = 23


    def forward():
        GPIO.output(Motor2F,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

    def reverse():
        GPIO.output(Motor2F,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

    def right():
        GPIO.output(Motor1F,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

    def left():
        GPIO.output(Motor1F,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

    def release():
        GPIO.output(Motor1E, GPIO.LOW)
        GPIO.output(Motor2E, GPIO.LOW)


