import RPi.GPIO as GPIO
import time

# Define GPIO pins for sensor
TRIG = 16
ECHO = 20
PIR_PIN = 18  # PIR sensor pin

# Define static variables
max_dist = 20
min_dist = 2
alpha = 0.2
percentage_full = 0
update_threshold = 5  # Initial threshold value
pir_wait_time = 5  # Wait time after PIR detection in seconds
open_count = 0  # Counter for lid openings

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(PIR_PIN, GPIO.IN)  # Set PIR pin as input
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH)

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

def calculate_fullness_percentage(dist, current_percentage):
    # Assuming 2 cm is 0% full and 20 cm is 100% full
    percentage = (dist - min_dist) / (max_dist - min_dist) * 100
    new_percentage = alpha * percentage + (1 - alpha) * current_percentage
    return max(0, min(100, new_percentage))  # Ensure the result is between 0 and 100

def calculate_update_threshold(dist):
    # Adjust the threshold based on the distance
    return max(1, min(10, update_threshold - (dist - min_dist) / (max_dist - min_dist) * 5))

def should_update_display(new_percentage, old_percentage, dist):
    threshold = calculate_update_threshold(dist)
    return abs(new_percentage - old_percentage) >= threshold

def pir_triggered(dist, open_count):
    if GPIO.input(PIR_PIN):
        if 30 <= dist <= 100:
            open_count += 1
            print("Lid opened! Count:", open_count)
            
            # Wait for a few seconds before checking again
            time.sleep(pir_wait_time)
    else:
        print('No movement')

    return open_count


