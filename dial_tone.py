#! /usr/bin/python3

import pygame
from config import DIAL_TONE
from config import DIAL_TONE_FILE


class DialTone(object):
    """
    DialTone class
    """

    def __init__(self, dial_tone_file=DIAL_TONE_FILE):
        self.dial_tone_file = dial_tone_file
        pygame.mixer.init()
        self.mixer = pygame.mixer

    def play_dial_tone(self):
        audio_file = self.dial_tone_file
        assert(audio_file != None)
        self.mixer.music.load(audio_file)
        self.mixer.music.play()
        # while pygame.mixer.music.get_busy() == True:
        #     continue
        self.state = DIAL_TONE
