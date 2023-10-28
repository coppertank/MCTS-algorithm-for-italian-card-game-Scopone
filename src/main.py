# pylint: disable=no-member

import os

import pygame
from controllers.main_controller import MainController


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    controller = MainController(None, None)
    controller.run()
    pygame.quit()


if __name__ == "__main__":
    main()
