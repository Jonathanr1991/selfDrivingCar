import RPi.GPIO as GPIO
from time import sleep


class CorvetteController():
    
    GPIO.setmode(GPIO.BOARD)
##right left dc motor pins
    Motor1F = 16
    Motor1B = 18
    Motor1E = 22

##foward right dc motor pins
    Motor2F = 19
    Motor2B = 21
    Motor2E = 23
    
    #GPIO pin setup
    GPIO.setup(Motor1F,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

    GPIO.setup(Motor2F,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)

    def forward(self):
        GPIO.output(self.Motor2F,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)

    def reverse(self):
        GPIO.output(self.Motor2F,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.HIGH)
        GPIO.output(self.Motor2E,GPIO.HIGH)

    def right(self):
        GPIO.output(self.Motor1F,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)

    def left(self):
        GPIO.output(self.Motor1F,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)

    def release(self):
        GPIO.output(self.Motor1E, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.LOW)


car = CorvetteController()
car.forward()
