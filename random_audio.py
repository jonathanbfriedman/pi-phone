#! /usr/bin/python3

from random import choice

from omxplayer.player import OMXPlayer

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
        try:
            player = OMXPlayer(audio_file)
            self.player = player
            self.state = PLAYING
        except:
            print("Error playing file " + audio_file)
