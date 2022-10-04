#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

time_unit_sec = 1

pin_led = 11


# Set up requested pin as output and set it low by default
def led_pin_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_led, GPIO.OUT)
    GPIO.output(pin_led, GPIO.LOW)

# Clear all GPIO settings
def led_pin_deinit():
    GPIO.cleanup()


# Switch on LED on 1 second
def led_blink_once():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)


# Switch on LED on 3 seconds (DASH symbol of Morse's alphabet)
def dash():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(3 * time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

# Switch on LED on 1 second (DOT symbol of Morse's alphabet)
def dot():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)


# Switch off LED on 1 second (pause between symbols of
# Morse's alphabet)
def dsh_dt_ps():
    GPIO.output(pin_led, GPIO.LOW)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)
