import RPi.GPIO as GPIO
import time

# Define GPIO pins for sensor
TRIG = 16
ECHO = 20
PIR_PIN = 18  # PIR sensor pin

# Define static variables
max_dist = 20
min_dist = 2
dist = 0
alpha = 0.2
percentage_full = 0
update_threshold = 5  # Initial threshold value
open_count = 0  # Counter for lid openings
lid_opened = False  # Flag to track if the lid is opened

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(PIR_PIN, GPIO.IN)  # Set PIR pin as input


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

def pir_callback(channel):
    global open_count, lid_opened
    if not lid_opened:
        open_count += 1
        lid_opened = True
        print("Lid opened! Count:", open_count)

if __name__ == '__main__':
    try:
        setup()
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=pir_callback, bouncetime=300)
        
        while True:
            dist = distance()
            print("Distance: {:.2f} cm".format(dist))

            if min_dist <= dist <= max_dist:
                new_percentage_full = calculate_fullness_percentage(dist, percentage_full)
                
                if should_update_display(new_percentage_full, percentage_full, dist):
                    percentage_full = new_percentage_full
                    print("Fullness Percentage: {:.2f}%".format(percentage_full))
                    
            elif lid_opened:
                lid_opened = False  # Reset the flag when the lid is closed

            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()