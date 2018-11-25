import sys
import time
import RPi.GPIO as GPIO
import random
import math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ControlPin = [7,22,23,24]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

GPIO.setup(8,GPIO.OUT)
GPIO.output(8,1)

Seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]
        
def blink():

        GPIO.output(8,0)
        time.sleep(0.25)
        GPIO.output(8,1)

def forwards():
	for i in range(1,40):
		for halfstep in range(0,8):
			for pin in range(0,4):
				GPIO.output(ControlPin[pin], Seq[halfstep][pin])
			time.sleep(0.001)
	blink()
	
def backwards():
	for i in range(1,40):
		for halfstep in range(7,-1,-1):
			for pin in range(0,4):
				GPIO.output(ControlPin[pin], Seq[halfstep][pin])
			time.sleep(0.001)
	blink()

while True:

        time.sleep(random.randint(5,10))

        t = random.randint(1,4)
        
        if t == 1:        
                forwards()
                time.sleep(random.randint(3,10))
                backwards()
        elif t == 2:
                backwards()
                time.sleep(random.randint(3,10))
                forwards()
        elif t == 4:
                backwards()
                forwards()
                time.sleep(2)
                forwards()
                backwards()
        else:
                blink()

GPIO.cleanup()                     
