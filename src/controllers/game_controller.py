from abstracts.controller import Controller
from enumerates.status import Status


class GameController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view, Status.GAME)

    def run(self):
        print('Game')
