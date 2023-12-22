import RPi.GPIO as GPIO

BUTTON_PIN = 17

def setup_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.LOW
