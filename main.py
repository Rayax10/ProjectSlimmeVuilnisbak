import sensor
import display
import button
import leds  # Importeer je LED-module

if __name__ == '__main__':
    try:
        sensor.setup()
        button.setup_button()
        leds.setup()  # Initialiseer de LED's

        percentage_full = 0  # Initieel percentage
        display_mode = "percentage"  # Houd bij welke modus wordt weergegeven

        while True:
            # Lees de knopstatus
            if button.is_button_pressed():
                # Wissel tussen statistieken en percentage weergeven
                if display_mode == "percentage":
                    display_mode = "statistics"
                    print("Switching to Statistics Mode")
                    # Display statistics on OLED
                    display.display_statistics([sensor.distance()])
                else:
                    display_mode = "percentage"
                    print("Switching to Percentage Mode")
                    # Display percentage on OLED
                    display.display_percentage(str(percentage_full))
                    print("Fullness Percentage: {:.2f}%".format(percentage_full))

            dist = sensor.distance()
            print("Distance: {:.2f} cm".format(dist))

            # Process PIR detection
            open_count = sensor.pir_triggered(dist, open_count)

            if sensor.min_dist <= dist <= sensor.max_dist:
                new_percentage_full = sensor.calculate_fullness_percentage(dist, percentage_full)

                if sensor.should_update_display(new_percentage_full, percentage_full, dist):
                    percentage_full = new_percentage_full

                    # Display percentage on OLED
                    if display_mode == "percentage":
                        display.display_percentage(str(percentage_full))
                        print("Fullness Percentage: {:.2f}%".format(percentage_full))
                        
                        # Update LED's based on percentage
                        led.leds(percentage_full)
                    else:
                        # Display statistics on OLED
                        display.display_statistics([dist])

            sensor.time.sleep(1)

    except KeyboardInterrupt:
        sensor.GPIO.cleanup()
        button.cleanup_button()
        leds.cleanup()  # Ruim de LED's op bij het afsluiten
