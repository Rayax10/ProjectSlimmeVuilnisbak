import RPi.GPIO as GPIO
import time

BUTTON_PIN = 22

def setup_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.LOW

if __name__ == '__main__':
    try:
        setup_button()

        while True:
            if is_button_pressed():
                print("Button is pressed!")

            time.sleep(0.4)  # Voeg een kleine vertraging toe om de CPU niet te zwaar te belasten
        

    except KeyboardInterrupt:
        GPIO.cleanup()
