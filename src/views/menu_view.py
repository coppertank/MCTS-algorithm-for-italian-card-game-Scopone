import os
import sys
import pygame
import pygame_menu
from abstracts.view import View
from enumerates.color import Color
from models import (DIFFICULTY, EASY, EXIT, EXTREME, GREEN, HARD, MEDIUM, MODE,
                    MODE_REVERSE, NEW_GAME, NO, ORANGE, PARTNER, PLAY, RED,
                    SIMULATE, SIMULATE_GAME, TEAM1, TEAM2, WATCH, YELLOW, YES,
                    menu_options)
from pygame_menu import themes

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

myimage = pygame_menu.baseimage.BaseImage(image_path=resource_path("assets/images/backgrounds/4.jpg"))

myfont = pygame_menu.font.FONT_FRANCHISE

mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = myimage
mytheme.font = myfont

class MenuView(View):
    def __init__(self):
        super().__init__()
        self.__menu = pygame_menu.Menu(
            'SCOPONE SCIENTIFICO',
            self.width, self.height, theme=mytheme)
        self.__create_menu_play()

    def draw(self):
        self.__menu.mainloop(self.screen)

    def __create_menu_play(self):
        self.__menu.clear()
        self.__menu.add.button(NEW_GAME, pygame_menu.events.EXIT)
        self.__menu.add.selector(
            MODE, menu_options[MODE], onchange=self.__change_menu)
        self.__menu.add.selector(PARTNER, menu_options[PARTNER])
        self.__menu.add.selector(DIFFICULTY, menu_options[DIFFICULTY],)
        self.__menu.add.button(EXIT, pygame_menu.events.EXIT)

    def __create_menu_simulate(self):
        self.__menu.clear()
        self.__menu.add.button(SIMULATE_GAME, pygame_menu.events.EXIT)
        self.__menu.add.selector(
            MODE, menu_options[MODE_REVERSE], onchange=self.__change_menu)
        self.__menu.add.selector(DIFFICULTY, menu_options[DIFFICULTY])
        self.__menu.add.selector(TEAM1, menu_options[TEAM1])
        self.__menu.add.selector(TEAM2, menu_options[TEAM2])
        self.__menu.add.selector(WATCH, menu_options[WATCH])
        self.__menu.add.button(EXIT, pygame_menu.events.EXIT)

    def __change_menu(self, _, index):
        if index == 1:
            self.__create_menu_play()
        elif index == 2:
            self.__create_menu_simulate()
        else:
            raise ValueError('Invalid index in mode selection')
