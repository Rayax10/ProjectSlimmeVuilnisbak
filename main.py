import sensor
import display
import button
import leds

if __name__ == '__main__':
    try:
        sensor.setup()
        button.setup_button()
        leds.setup()  # Initialiseer de LED's

        percentage_full = 0
        new_percentage_full = 0
        data = []

        display_mode = "percentage"

        while True:
            if button.is_button_pressed():
                if display_mode == "percentage":
                    display_mode = "statistics"
                    print("Switching to Statistics Mode")
                else:
                    display_mode = "percentage"
                    print("Switching to Percentage Mode")

            dist = sensor.distance()
            data.append(dist)
            print("Distance: {:.2f} cm".format(dist))

            open_count = sensor.pir_triggered(dist, sensor.open_count)

            if sensor.min_dist <= dist <= sensor.max_dist:
                new_percentage_full = sensor.calculate_fullness_percentage(dist, percentage_full)

                if sensor.should_update_display(new_percentage_full, percentage_full, dist):
                    percentage_full = new_percentage_full

                    if display_mode == "percentage":
                        display.display_percentage(str(percentage_full))
                        leds.leds(percentage_full)  # Stuur de LED's aan op basis van het percentage
                        print("Fullness Percentage: {:.2f}%".format(percentage_full))
                    else:
                        display.display_statistics(data)

            sensor.time.sleep(1)

    except KeyboardInterrupt:
        sensor.GPIO.cleanup()
        button.cleanup()
        leds.cleanup() 
