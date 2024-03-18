import sys
import os
import pygame

from script.map.objectDesign import *
from script.parameters import *
from script.general import *
from script.paths import *
from script.decorators import *


class MyGame:
    __version__ = "0.1"
    __author__ = 'dmkn96@icloud.com'
    __title__ = "My Game"

    def __init__(self):
        # Initialize the paths
        self.paths = Paths(os.path.dirname(__file__))

        # Initialize the settings
        readSettings(self)

        # Initialize the game
        pygameRun(self)


if __name__ == "__main__":
    MyGame()
