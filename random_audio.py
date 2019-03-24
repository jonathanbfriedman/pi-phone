#! /usr/bin/python3

import pygame
from random import choice

from glob import glob

from os import listdir
from os.path import isfile, join

from config import PLAYING
from config import FILETYPES


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
        files_list = []
        for filetype in FILETYPES:
            files_list.extend(glob(join(audio_directory, '*.' + filetype)))
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
