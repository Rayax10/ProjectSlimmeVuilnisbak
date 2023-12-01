import RPi.GPIO as GPIO
import time
 
# Define GPIO pins for sensor
TRIG = 16
ECHO = 20
 
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
 
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
 
if __name__ == '__main__':
    try:
        setup()
        while True:
            dist = distance()
            print("Distance: ", dist, " cm")
            # Add logic to determine fullness percentage based on distance
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()