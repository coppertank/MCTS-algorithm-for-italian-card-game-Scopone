from dataclasses import dataclass

from models import (DIFFICULTY, EASY, EXIT, EXTREME, GREEN, HARD, MEDIUM, MODE,
                    NEW_GAME, NO, ORANGE, PARTNER, PLAY, RED, SIMULATE,
                    SIMULATE_GAME, TEAM1, TEAM2, WATCH, YELLOW, YES,
                    menu_options)


@dataclass
class MenuModel:
    def __init__(self) -> None:
        self.__mode = PLAY
        self.__partner = GREEN
        self.__difficulty = EASY
        self.__team1 = GREEN
        self.__team2 = GREEN
        self.__watch = YES

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = value

    @property
    def partner(self):
        return self.__partner

    @partner.setter
    def partner(self, value):
        self.__partner = value

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value

    @property
    def team1(self):
        return self.__team1

    @team1.setter
    def team1(self, value):
        self.__team1 = value

    @property
    def team2(self):
        return self.__team2

    @team2.setter
    def team2(self, value):
        self.__team2 = value

    @property
    def watch(self):
        return self.__watch

    @watch.setter
    def watch(self, value):
        self.__watch = value
