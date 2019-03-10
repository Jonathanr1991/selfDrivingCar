import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1F = 16
Motor1B = 18
Motor1E = 22

Motor2F =19
Motor2B = 21
Motor2E = 23

GPIO.setup(Motor1F,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2F,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print "turn left"


GPIO.output(Motor1F,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)
print "turn right"

GPIO.output(Motor1F,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
sleep(2)

print "turn foward"


GPIO.output(Motor2F,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
sleep(2)

print "turn backward"

GPIO.output(Motor2F,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)
sleep(2)
print "stop"

GPIO.output(Motor1E, GPIO.LOW)

GPIO.output(Motor2E, GPIO.LOW)


GPIO.cleanup()
