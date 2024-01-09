import RPi.GPIO as GPIO
import time
import random

led_pins = [25, 12 , 26]
#12 geel, 25 groen, 26 rood

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led_pins, GPIO.OUT)

def leds(percentage):
    if percentage <= 33:
        GPIO.output(led_pins[0], GPIO.HIGH)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.LOW)
    elif percentage <= 80:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.HIGH)
        GPIO.output(led_pins[2], GPIO.LOW)
    else:
        GPIO.output(led_pins[0], GPIO.LOW)
        GPIO.output(led_pins[1], GPIO.LOW)
        GPIO.output(led_pins[2], GPIO.HIGH)

