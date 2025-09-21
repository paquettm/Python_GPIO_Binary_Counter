import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Assign your GPIO pins (change as needed for your wiring)
LED_PINS = [17, 18, 22]  # Example GPIO pins for 3 LEDs

# Set each pin as output
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

def displayBin(n):
    """
    Displays the binary representation (3 bits) of integer n (0-7) on 3 LEDs.
    :param n: integer value from 0 to 7
    """
    # Ensure n is within the correct range
    if n < 0 or n > 7:
        print("Value out of range (0-7).")
        return

    # Convert n to binary, pad to 3 places
    bin_str = f"{n:03b}"
    
    # Set each LED according to corresponding bit
    for i, pin in enumerate(LED_PINS):
        GPIO.output(pin, int(bin_str[2-i]))

# Example usage: display number 5 (binary 101)
displayBin(5)
time.sleep(5)  # LEDs stay on for 5 seconds

# Turn off LEDs and clean up
for pin in LED_PINS:
    GPIO.output(pin, 0)
GPIO.cleanup()