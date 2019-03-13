#! /usr/bin/python3

# Script to manage phone hook status as user input

import RPi.GPIO as GPIO
from signal import pause

GPIO.setmode(GPIO.BCM)


class Hook(object):
    """
    Hook class
    """

    def __init__(self, hook_pin):
        self.hook_pin = hook_pin

        # Set up GPIO
        switch = GPIO.setup(self.hook_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.switch = switch
