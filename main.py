import sensor
import display

if __name__ == '__main__':
    try:
        sensor.setup()
        percentage_full = 0  # Initieel percentage

        while True:
            dist = sensor.distance()
            print("Distance: {:.2f} cm".format(dist))

            # Process PIR detection
            open_count = sensor.pir_triggered(dist, open_count)

            if sensor.min_dist <= dist <= sensor.max_dist:
                new_percentage_full = sensor.calculate_fullness_percentage(dist, percentage_full)

                if sensor.should_update_display(new_percentage_full, percentage_full, dist):
                    percentage_full = new_percentage_full

                    # Display percentage on OLED
                    display.display_percentage(str(percentage_full))
                    print("Fullness Percentage: {:.2f}%".format(percentage_full))

                    # Display statistics on OLED (add this line)
                    display.display_statistics([dist])

            sensor.time.sleep(1)
    except KeyboardInterrupt:
        sensor.GPIO.cleanup()
