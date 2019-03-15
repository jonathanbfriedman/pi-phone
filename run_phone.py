#! /usr/bin/python3

# Script to run phone

from phone import Phone

from config import HOOK_PIN
from config import RINGER_PIN

from config import DIAL_TONE_FILE
from config import AUDIO_DIRECTORY

from config import DIAL_TONE
from config import PLAYING

from config import RING_MIN
from config import RING_MAX
from config import RING_ON
from config import RING_OFF


# Set variables
ring_on = RING_ON
ring_off = RING_OFF
ring_min = RING_MIN
ring_max = RING_MAX

ringer_pin = RINGER_PIN

hook_pin = HOOK_PIN

audio_directory = AUDIO_DIRECTORY

dial_tone_file = DIAL_TONE_FILE

# Create phone instance
phone = Phone(ring_min, ring_max,
        ring_on, ring_off,
        ringer_pin, hook_pin,
        dial_tone_file, audio_directory)

# Run phone
phone.run()
