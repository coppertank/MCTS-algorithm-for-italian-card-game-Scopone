from abstracts.controller import Controller
from enumerates.status import Status


class ResultsController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view, Status.RESULTS)

    def run(self):
        print('Results')
