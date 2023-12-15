import busio
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import adafruit_ssd1306
from statistics import mean, median, mode

SDA = 2
SCL = 3

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
 
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
 
# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
 
display.show()
 
# Create blank image for drawing
width = display.width
height = display.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on the image.
draw = ImageDraw.Draw(image)

def display_statistics(data):
    # Calculate statistics
    mean_value = mean(data)
    median_value = median(data)
    mode_value = mode(data)

    # Display statistics on OLED
    display_text = f"Mean: {mean_value:.2f}\nMedian: {median_value}\nMode: {mode_value}"

    # Load font.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)

    # Draw a white background.
    draw.rectangle((0, 0, width, height), outline=255, fill=255)

    # Define text and get its size.
    text_width, text_height = draw.textsize(display_text, font=font)

    # Calculate text position to center it on the display.
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw the text on the image.
    draw.multiline_text((x, y), display_text, font=font, fill=0)

    # Display the image on the OLED.
    display.image(image)
    display.show()
    
def display_percentage(percentage):
    # Load font.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
 
    # Draw a white background.
    draw.rectangle((0, 0, width, height), outline=255, fill=255)
 
    # Define text and get its size.
    text = percentage
    text_width, text_height = draw.textsize(text, font=font)
 
    # Calculate text position to center it on the display.
    x = (width - text_width) / 2
    y = (height - text_height) / 2
 
    # Draw the text on the image.
    draw.text((x, y), text, font=font, fill=0)
 
    # Display the image on the OLED.
    display.image(image)
    display.show()


