#! /usr/bin/python3
# https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import Button
from subprocess import check_call
from signal import pause

SHUTDOWN_PIN = 18 # GPIO numbering
HOLD_TIME = 2 # seconds

def shutdown():
        check_call(['sudo', 'poweroff'])

shutdown_btn = Button(SHUTDOWN_PIN, hold_time=HOLD_TIME)
shutdown_btn.when_held = shutdown

pause()
