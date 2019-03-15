#! /usr/bin/python3

# Script to manage ringing

import RPi.GPIO as GPIO

from signal import pause
from config import RINGING
from time import sleep
from random import uniform

from config import RING_MIN
from config import RING_MAX

from config import RING_ON
from config import RING_OFF

from config import RINGER_PIN


class Ringer(object):
    """
    Ringer class
    """

    def __init__(self, ring_on=RING_ON, ring_off=RING_OFF, ringer_pin=RINGER_PIN,
            ring_min=RING_MIN, ring_max=RING_MAX):
        self.ring_on = ring_on
        self.ring_off = ring_off
        self.ring_min = ring_min
        self.ring_max = ring_max
        self.ringer_pin = ringer_pin

        # Set ringer pin as output
        GPIO.setup(self.ringer_pin, GPIO.OUT)
        GPIO.output(self.ringer_pin, GPIO.LOW)

    def play_ringer(self):
        # Wait a random amount
        wait = uniform(self.ring_min, self.ring_max)
        print("Playing ringer in " + str(wait)  + " minutes")
        sleep(wait*60) # convert minutes to seconds
        self.state = RINGING
        while self.state == RINGING:
            print("Ring ring...")
            GPIO.output(self.ringer_pin, GPIO.HIGH)
            sleep(self.ring_on)
            GPIO.output(self.ringer_pin, GPIO.LOW)
            sleep(self.ring_off)
