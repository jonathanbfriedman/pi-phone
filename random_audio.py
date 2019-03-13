#! /usr/bin/python3

import pygame
from random import choice

from os import listdir
from os.path import isfile, join

from config import PLAYING


class RandomAudio(object):
    """
    Random Audio class
    """

    def __init__(self, audio_directory):
        self.audio_directory = audio_directory
        pygame.mixer.init()
        self.mixer = pygame.mixer

    def get_audio_list(self):
        audio_directory = self.audio_directory
        files_list = [f for f in listdir(audio_directory) if isfile(join(audio_directory, f))]
        self.files_list = files_list
        return files_list

    def select_audio(self):
        try:
            self.files_list
            return choice(self.files_list)
        except AttributeError:
            return choice(self.get_audio_list())
        
    def play_random_audio(self):
        audio_file = join(self.audio_directory, self.select_audio())
        assert(audio_file != None)
        self.mixer.music.load(audio_file)
        self.mixer.music.play()
        # while pygame.mixer.music.get_busy() == True:
        #     continue
        self.state = PLAYING
