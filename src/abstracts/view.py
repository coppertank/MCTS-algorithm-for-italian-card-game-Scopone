from abc import abstractmethod

import pygame
from config import FONT_SIZE, FPS, WINDOW_HEIGHT, WINDOW_WIDTH
# pylint: disable=import-error
from interfaces.view_interface import ViewInterface


class View(ViewInterface):
    def __init__(self):
        self.height = WINDOW_HEIGHT
        self.width = WINDOW_WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font_size = FONT_SIZE
        self.font = pygame.font.SysFont(None, self.font_size)
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)
        self.status = None

    @abstractmethod
    def draw(self):
        pass
