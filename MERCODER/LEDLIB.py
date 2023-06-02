#!/usr/bin/env python3
# MERCODER LED LIGHT BOARD LIBRARY
#
# MERCODER's LEDLIB began with:
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import PixelStrip, Color
import argparse
import random

# LED lights configuration:
LED_COUNT = 450        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#############   LED Library for 22x18 LED light board  #############
ROWS = 22
COLS = 18

###  Color(R,G,B) with each red, green, and blue
###               taking on an integer 0-255
RED = Color(255,0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)
WHITE = Color(255,255,255)
BLACK = Color(0,0,0)
ORANGE = Color(105,40,0)
YELLOW = Color(255,155,0)
DARKBLUE = Color(0,0,128)
PINK = Color(255,0,255)


# Create NeoPixel object with appropriate configuration.
lights = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

# Intialize the library (must be called once before other functions).
lights.begin()

##########  Default test functions that came with the LED library

# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=10):
    """Wipe color across display a pixel at a time."""
    for i in range(lights.numPixels()):
        lights.setPixelColor(i, color)
        lights.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, lights.numPixels(), 3):
                lights.setPixelColor(i + q, color)
            lights.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, lights.numPixels(), 3):
                lights.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(lights.numPixels()):
            lights.setPixelColor(i, wheel((i + j) & 255))
        lights.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(lights.numPixels()):
            lights.setPixelColor(i, wheel(
                (int(i * 256 / lights.numPixels()) + j) & 255))
        lights.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, lights.numPixels(), 3):
                lights.setPixelColor(i + q, wheel((i + j) % 255))
            lights.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, lights.numPixels(), 3):
                lights.setPixelColor(i + q, 0)


# SABOARD flicker a pixel bouncing randomly around
#     c1 is the color of the pixel, c2 is the background color
def flicker(c1,c2):
    row = ROWS//2
    col = COLS//2
    setColor(c2)
    setColorAt(row,col,c1)
    lights.show()
    for loop in range(1000):
        time.sleep(.1)
        setColorAt(row,col,c2)
        row = row + random.randrange(5) - 2
        if row < 0:
            row = 0
        if row >= ROWS:
            row = ROWS -1
        col = col + random.randrange(5) - 2
        if col < 0:
            col = 0
        if col >= COLS:
            col = COLS -1
        setColorAt(row,col,c1)
        lights.show()

# SABOARD setColor turns the whole board to the given color
def setColor(color):
    for row in range(ROWS):
        for col in range(COLS):
            lights.setPixelColor(row+col*25,color)
    lights.show()

# SABOARD setColColor turns one column the given color
def setColColor(col,color):
    """Set col a color """
    for i in range(ROWS):
        lights.setPixelColor(i+col*25,color)
    lights.show()

# SABOARD setRowColor turns one row the given color
def setRowColor(row,color):
    """Set row a color"""
    for i in range(0,450,50):
        lights.setPixelColor(i + 21 - row,color)
        lights.setPixelColor(i + 25 + row,color)
    lights.show()

# SABOARD setColorAt(row,col,color)
def setColorAt(row,col,color):
    """ Set one pixel at (row,col) to given color """
    if col%2 == 0:
        lights.setPixelColor(21-row + col//2 * 50,color)
    else:
        lights.setPixelColor(25+row + col//2 * 50,color)

# SABOARD colorWipeLR wipes a specifed color across the board LR
def colorWipeLR(color):
    for col in range(COLS):
        setColColor(col,color)

# SABOARD colorWipeDown wipes a specifed color across board from top down 
def colorWipeDown(color):
    for row in range(ROWS):
        setRowColor(row,color)

# SABOARD makeBox places a rectangular box on LED board with
#         upper left corner at (row,col) and
#         has specified width, height, and color
def makeBox(row,col,width,height,color):
    for r in range(height):
        for c in range(width):
            setColorAt(row+r,col+c,color)
    lights.show()

# SABOARD checkerBoard fills LED board with 2x2 boxes alternating colors
def checkerBoard(color1,color2):
    order = 0
    for r in range(0,ROWS,2):
        for c in range(0,COLS,2):
            if order%2 == 0:
                makeBox(r,c,2,2,color1)
            else:
                makeBox(r,c,2,2,color2)
            order = order + 1

# SABOARD randColor returns a random Color
def randColor():
    r=random.randrange(256)
    g=random.randrange(256)
    b=random.randrange(256)
    return Color(r,g,b)
