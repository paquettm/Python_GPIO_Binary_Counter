# Intro to Python in Context - Variables, Function, Classes, Objects, Lists, Libraries, GPIO

You have learned and observed a few things about Python up until now.
Today, you will be challenged and not be given so many instructions.
But you are ready.

## Material needed:

- Raspberry Pi
- Breadboard
- LEDS
- resistors

**Note that the list does not include a Linux computer this time around... so you need to do this exclusively on your Raspberry Pi single-board computer.**

## Part 1: Python and Magic Functions

### Task 1: Run the Code

Perform all operations needed to clone the repository to your computer and run the `main.py` program.
You may need to
- go on the web
- find the repository URL
- clone the repository
- create a virtual environment
- install packages with pip
- etc.

## Task 2: Analyse the Code and its Functionality

- Read the code
- Associate each line of the code with the correct output
- Explain how each object of class example has a unique identifier that will never be used twice in a same program
- Explain why the list counter count class property and the list length are the same.

## Task 3: Improve the Code

- Modify the code to accomplish the following:
    - Add a global boolean variable named hear_speech
    - Add code to remove speech when hear_speech is False
    - Identify sequences of identical instructions and replace these by loops containing a single instruction

# Part 2: LED binary counter

Recall you are still using your Raspberry Pi for this lab.

A binary counter displays a decimal number by showing its value as a sequence of bits (0s and 1s), where each bit represents a power of two and their sum equals the original decimal number.

## Binary Counter Basics
- Each bit in the counter represents a specific place value: the rightmost bit is $$2^0$$ (ones place), then $$2^1$$ (twos place), $$2^2$$ (fours), etc.
- When the counter increments, the bits change state, "overflowing" to the next higher place, just as decimal digits do.

So when a 9 would become the number 10, we say it overflows, and we have to increment the next position over, e.g., 29 increases to 30.

### Converting Binary to Decimal
- To read a binary counter’s output as a decimal, multiply each bit by its corresponding power of two and sum them.
- For example, the binary value $$1011$$ is calculated as:
  $$
  1\times2^3 + 0\times2^2 + 1\times2^1 + 1\times2^0 = 8 + 0 + 2 + 1 = 11
  $$
  So, a counter displaying $$1011$$ equals decimal 11.

### Displaying Decimal Numbers
- The binary counter itself shows values only in binary; conversion to decimal requires interpreting the bits as described.
- In electronics or programming, binary counters are often used for precise tracking because digital systems handle binary naturally.

In summary, a binary counter’s series of bits must be converted by evaluating their weighted sum to display the decimal equivalent.

## Task 1: Build the circuit

Turn off your Raspberry pi before making any connection to the Raspberry Pi.

Connect RPi GPIO to a few discrete components to create a 3-bit binary display. In other words, connect 3 LEDs and resistors to different control pins on the RPi.
The build should contain a breadboard, 3 LEDs, 3 resistors (current-limiting), and wires.

You may need to find information about the Raspberry Pi GPIO header pinout.

Wire things up while the RPi is powered off.

## Task 2: Learn abou the GPIO

Open the file `LED_Display.py`.
Read the code and attempt to interpret it.

**Important note: Raspberry Pi 4 requires de library `RPi.GPIO` whereas Raspberry Pi 5 requires the library `rpi-lgpio`.**

Install the libraries in the virtual environment to make the code runnable.

Run the code.

Associate each action that you observe to the lines in the code.

Are the LEDs lighting up? If not, do the connections correspond to the LOGICAL pin numbering in the GPIO pinout? Are your circuits complete? Are the LEDs wired the correctly?

## Task 3: Modify `main.py`

Add the necessary code to configure the GPIO for your circuit in the `main.py` file.

Add a function to display small numbers on your LEDS to the `main.py` file.

Add instructions to display the object count on the binary LED display.

Verify that your code is running as intended. If not, debug.

Repeat until the program is running as intended.

Part 3: Reflection log

Update your reflection log and discuss today's activity.
