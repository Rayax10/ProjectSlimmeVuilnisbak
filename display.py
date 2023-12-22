import busio
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import adafruit_ssd1306
from statistics import mean, median, mode

SDA = 2
SCL = 3

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the first SSD1306 OLED class for statistics.
display_stats = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Create the second SSD1306 OLED class for percentage.
display_percentage = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3D)  # Use the appropriate I2C address for the second display

# Clear the displays. Always call show after changing pixels to make the display update visible!
display_stats.fill(0)
display_stats.show()

display_percentage.fill(0)
display_percentage.show()

# Create blank images for drawing on each display
width_stats, height_stats = display_stats.width, display_stats.height
image_stats = Image.new('1', (width_stats, height_stats))

width_percentage, height_percentage = display_percentage.width, display_percentage.height
image_percentage = Image.new('1', (width_percentage, height_percentage))

# Get drawing objects to draw on the images.
draw_stats = ImageDraw.Draw(image_stats)
draw_percentage = ImageDraw.Draw(image_percentage)

def display_statistics(data):
    # Calculate statistics
    mean_value = mean(data)
    median_value = median(data)
    mode_value = mode(data)

    # Display statistics on the statistics OLED.
    display_text = f"Mean: {mean_value:.2f}\nMedian: {median_value}\nMode: {mode_value}"

    # Load font.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)

    # Draw a white background.
    draw_stats.rectangle((0, 0, width_stats, height_stats), outline=255, fill=255)

    # Define text and get its size.
    text_width, text_height = draw_stats.textsize(display_text, font=font)

    # Calculate text position to center it on the display.
    x = (width_stats - text_width) / 2
    y = (height_stats - text_height) / 2

    # Draw the text on the image.
    draw_stats.multiline_text((x, y), display_text, font=font, fill=0)

    # Display the image on the statistics OLED.
    display_stats.image(image_stats)
    display_stats.show()

def display_percentage_value(percentage):
    # Load font.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
 
    # Draw a white background.
    draw_percentage.rectangle((0, 0, width_percentage, height_percentage), outline=255, fill=255)
 
    # Define text and get its size.
    text = percentage
    text_width, text_height = draw_percentage.textsize(text, font=font)
 
    # Calculate text position to center it on the display.
    x = (width_percentage - text_width) / 2
    y = (height_percentage - text_height) / 2
 
    # Draw the text on the image.
    draw_percentage.text((x, y), text, font=font, fill=0)
 
    # Display the image on the percentage OLED.
    display_percentage.image(image_percentage)
    display_percentage.show()

