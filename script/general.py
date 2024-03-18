import pygame
from script.map.objectDesign import *
import configparser


def readSettings(self):
    self.settings = configparser.ConfigParser()
    self.settings.read(self.paths.settingsPath)


def mapGrid(self, window_size):
    for x in range(0, window_size[0], BlockParameters.blockSize):
        for y in range(0, window_size[1], BlockParameters.blockSize):
            rect = pygame.Rect(x, y, BlockParameters.blockSize, BlockParameters.blockSize)
            pygame.draw.rect(self.screen, BlockParameters.blockColor, rect, 1)


def pygameRun(self):
    """
    Run the game using pygame
    :param self:
    :return:
    """
    # Step 1 : Initialize the game
    pygame.init()

    # Step 2 : Set the window size
    self.window_size = (self.settings.getint('window', 'width'), self.settings.getint('window', 'height'))

    # Step 3 : Set the window policy
    self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

    # Step 4 : Set the window icon
    self.window_icon = pygame.image.load(self.paths.iconPath)

    # Step 5 : Set the window title
    pygame.display.set_caption(self.__title__)

    # Step 6 : Draw the map grid
    mapGrid(self, self.screen.get_size())

    # Step 6 : Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                resizeLogic(self, event)
                mapGrid(self, self.screen.get_size())

        pygame.display.flip()

    # Step 7 : Quit the game
    pygame.quit()


def resizeLogic(self, event) -> int:
    """
    Resize the game logic
    :param self:
    :param event:
    :return:
    """
    new_width = max(event.w, self.settings.getint('window', 'minWidth'))
    new_height = max(event.h, self.settings.getint('window', 'minHeight'))

    if new_width != event.w or new_height != event.h:
        pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
    else:
        pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    return 0
