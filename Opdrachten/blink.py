import RPi.GPIO as GPIO
import time

LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)

time.sleep(3)

GPIO.output(LED, GPIO.LOW)