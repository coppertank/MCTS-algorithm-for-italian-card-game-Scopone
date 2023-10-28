from abstracts.controller import Controller
from enumerates.status import Status


class MenuController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view, Status.MENU)

    def run(self):
        self.view.draw()
