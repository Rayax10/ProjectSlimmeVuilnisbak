import RPi.GPIO as GPIO
import time

# Define GPIO pins for sensor
TRIG = 16
ECHO = 20

# Define static variables
max_dist = 20
min_dist = 0
dist = 0
average_list = []
average = 0

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

def calculate_fullness_percentage(dist):
    # Assuming 0 cm is 0% full and 20 cm is 100% full
    percentage = 100 - (dist / max_dist) * 100
    return max(0, min(100, percentage))  # Ensure the result is between 0 and 100

if __name__ == '__main__':
    try:
        setup()
        while True:
            dist = distance()
            print("Distance: ", dist, " cm")

            if dist > max_dist:
                print('OverRange')
            if dist < min_dist:
                print('UnderRange')
            if dist in range(0, 21):
                average_list.append(dist)

            # Calculate average
            average = sum(average_list) / len(average_list)
            print("Average Distance: ", average, " cm")

            # Calculate and print fullness percentage
            percentage_full = calculate_fullness_percentage(average)
            print("Fullness Percentage: {:.2f}%".format(percentage_full))

            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
