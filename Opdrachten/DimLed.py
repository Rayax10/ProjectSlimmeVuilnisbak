import RPi.GPIO as GPIO
import time

dutyCycle = 0
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
LED = GPIO.PWM(26, 100)
LED.start(dutyCycle)

while True:
    dutyCycle += 1
    LED.ChangeDutyCycle(dutyCycle % 100)
    time.sleep(0.01)
    
