#! /usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from time import sleep

from multiprocessing import Process

# Script to control landline phone operation
# See Github repository for more information:
# https://github.com/jonathanbfriedman/pi-phone

from signal import pause

from config import RING_MIN
from config import RING_MAX
from config import RING_ON
from config import RING_OFF

from config import RINGER_PIN
from config import HOOK_PIN

from config import AUDIO_DIRECTORY
from config import DIAL_TONE_FILE

from hook import Hook
from ringer import Ringer
from random_audio import RandomAudio
from dial_tone import DialTone

from config import PLAYING
from config import RINGING
from config import DIAL_TONE
from config import SILENCE

# States
# 1. Phone is on hook
# 2. Phone is off hook
# 3. Phone is ringing
# 4. Phone is playing audio

# dial_tone.py
# ring.py
# audio.py
# hook.py



class Phone(Ringer, Hook, DialTone, RandomAudio):
    """
    Phone class
    """

    def __init__(self, ring_min=RING_MIN, ring_max=RING_MAX,
            ring_on=RING_ON, ring_off=RING_OFF,
            ringer_pin=RINGER_PIN, hook_pin=HOOK_PIN,
            dial_tone_file=DIAL_TONE_FILE, audio_directory=AUDIO_DIRECTORY):

        self.ring_on = ring_on
        self.ring_off = ring_off
        self.ring_min = ring_min
        self.ring_max = ring_max

        self.ringer_pin = ringer_pin

        self.hook_pin = hook_pin

        self.audio_directory = audio_directory

        self.dial_tone_file = dial_tone_file

        Ringer.__init__(self, self.ring_on, self.ring_off, self.ringer_pin)
        Hook.__init__(self, self.hook_pin)
        DialTone.__init__(self, self.dial_tone_file)
        RandomAudio.__init__(self, self.audio_directory)

        self.state = SILENCE

        GPIO.setup(self.hook_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def off_to_on_hook(self):
        print("off_to_on_hook called")
        # Stop audio (works for dial tone or other audio)
        self.mixer.music.stop()
        # Start the ringer protocol as a process
        ringer_process = Process(target=self.play_ringer, daemon=True)
        ringer_process.start()
        self.state = RINGING
        # ringer_process.join()
        self.ringer_process = ringer_process

    def on_to_off_hook(self):
        print("on_to_off_hook called")
        # If ringer is playing:
        if self.state == RINGING:
            # Stop ringer process
            self.ringer_process.terminate()
            # Force ringer pin output to low
            GPIO.output(self.ringer_pin, GPIO.LOW)
        if self.state != PLAYING:
            # Play random audio
            self.state = PLAYING
            self.play_random_audio()
            while self.mixer.music.get_busy():
                sleep(0.1)
            self.state = DIAL_TONE
            self.play_dial_tone()


    def hook_change(self, channel):
        print("hook change callback called")
        try:
            self.ringer_process.terminate()
        except:
            pass
        assert(channel == self.hook_pin)
        if GPIO.input(self.hook_pin):
            self.off_to_on_hook()
        else:
            self.on_to_off_hook()

    def run(self):
        print("Running pi phone...")
        # Call hook_change if phones is taken off hook or put back on
        if GPIO.input(self.hook_pin):
            ringer_process = Process(target=self.play_ringer)
            ringer_process.start()
            self.ringer_process = ringer_process
        else:
            # Play random audio
            self.state = PLAYING
            self.play_random_audio()
            while self.mixer.music.get_busy():
                sleep(0.2)
            self.state = DIAL_TONE
            self.play_dial_tone()

        try:
            GPIO.add_event_detect(self.hook_pin, GPIO.BOTH, callback=self.hook_change, bouncetime=50)
            # self.hook_change(self.hook_pin)
            pause()
        except KeyboardInterrupt:
            GPIO.cleanup()
        GPIO.cleanup()
