#! /usr/bin/python3

from unittest import TestCase

from time import sleep

import RPi.GPIO as GPIO

from dial_tone import DialTone
from random_audio import RandomAudio
from hook import Hook
from ringer import Ringer
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


class TestDialTone(TestCase):
    """
    DialTone class tests
    """

    def setUp(self):
        self.dial_tone_file = DIAL_TONE_FILE

    def test_play(self):
        dial_tone = DialTone(self.dial_tone_file)
        dial_tone.play_dial_tone()
        sleep(5)
        self.assertEqual(dial_tone.state, DIAL_TONE)
        dial_tone.mixer.music.stop()


class TestRandomAudio(TestCase):
    """
    RandomAudio class tests
    """

    def setUp(self):
        self.audio_directory = AUDIO_DIRECTORY

    def test_play_random_audio(self):
        random_audio = RandomAudio(self.audio_directory)
        random_audio.play_random_audio()
        sleep(5)
        self.assertEqual(random_audio.state, PLAYING)
        random_audio.player.stop()


class TestHook(TestCase):
    """
    Hook class tests
    """

    def setUp(self):
        self.hook_pin = HOOK_PIN

    def test_hook(self):
        hook = Hook(self.hook_pin)


class TestPhone(TestCase):
    """
    Phone class tests
    """

    def setUp(self):
        self.ring_on = RING_ON
        self.ring_off = RING_OFF
        self.ring_min = RING_MIN
        self.ring_max = RING_MAX

        self.ringer_pin = RINGER_PIN

        self.hook_pin = HOOK_PIN

        self.audio_directory = AUDIO_DIRECTORY

        self.dial_tone_file = DIAL_TONE_FILE

    def test_run(self):
        phone = Phone(self.ring_min, self.ring_max,
                self.ring_on, self.ring_off,
                self.ringer_pin, self.hook_pin,
                self.dial_tone_file, self.audio_directory)
        phone.run()


class TestRinger(TestCase):
    """
    Ringer class tests
    """

    def setUp(self):
        self.ring_on = RING_ON
        self.ring_off = RING_OFF
        self.ring_min = RING_MIN
        self.ring_max = RING_MAX

        self.ringer_pin = RINGER_PIN

    def test_ringer(self):
        ringer = Ringer(self.ring_on, self.ring_off,
                self.ringer_pin, self.ring_min, self.ring_max)
        ringer.play_ringer()
