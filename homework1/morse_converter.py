#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

print ("Hello, world!")
led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()
