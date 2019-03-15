#! /usr/bin/python3

# Configuration file

# Ring interval (in minutes)
RING_MIN = 5
RING_MAX = 7

# Ring style (in seconds)
RING_ON = 2
RING_OFF = 5*60

# Ringer output pin
RINGER_PIN = 14 # GPIO numbering

# Hook input pin
HOOK_PIN = 4 # GPIO numbering

# Set audio directory (full path)
AUDIO_DIRECTORY = "/home/pi/share/audio"

# Set dial tone file location (full path)
DIAL_TONE_FILE = "/home/pi/sounds/dial_tone_1min.mp3"

# Some state variables
PLAYING = 0
RINGING = 1
DIAL_TONE = 2
SILENCE = 3
