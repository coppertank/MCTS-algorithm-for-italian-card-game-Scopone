from abc import abstractmethod

from interfaces.controller_interface import ControllerInterface


class Controller(ControllerInterface):
    def __init__(self, model, view, status):
        self.model = model
        self.view = view
        self.status = status

    @abstractmethod
    def run(self):
        pass
