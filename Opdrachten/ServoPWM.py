import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
servo = GPIO.PWM(12,50)
servo.start(5)
time.sleep(2)
servo.ChangeDutyCycle(20)
time.sleep(2)
servo.ChangeDutyCycle(7.5)
time.sleep(2)

GPIO.cleanup()
