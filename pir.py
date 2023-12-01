import RPi.GPIO as GPIO
import sys
import signal
import time

PIR = 13
LED1 = 21
LED2 = 20
LED3 = 25
LED4 = 26
LED5 = 12

LEDS = [LED1, LED2, LED3, LED4, LED5]

def pir_triggered(pin):
    count = 0
    if GPIO.input(pin):
        count = count + 1
        GPIO.setup(LEDS, GPIO.OUT)
        GPIO.output(LEDS, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LEDS, GPIO.LOW)
        time.sleep(30)
        print('movement')
    else:
        print('no movement')
        
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIR, GPIO.IN)
GPIO.add_event_detect(PIR, GPIO.BOTH, callback=pir_triggered)

signal.pause()
