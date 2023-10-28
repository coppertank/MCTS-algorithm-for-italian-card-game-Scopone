from abstracts.controller import Controller
from controllers.game_controller import GameController
from controllers.menu_controller import MenuController
from controllers.results_controller import ResultsController
from enumerates.status import Status
from models.game_model import GameModel
from models.menu_model import MenuModel
from models.results_model import ResultsModel
from views.game_view import GameView
from views.menu_view import MenuView
from views.results_view import ResultsView


class MainController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view, Status.MENU)
        self.menu_controller = None
        self.game_controller = None
        self.results_controller = None
        self.set_menu_controller()
        self.set_game_controller()
        self.set_results_controller()

    def run(self):
        while True:
            if self.status == Status.MENU:
                self.menu_controller.run()
                self.status = self.menu_controller.status
            elif self.status == Status.GAME:
                self.game_controller.run()
                self.status = self.game_controller.status
            elif self.status == Status.RESULTS:
                self.results_controller.run()
                self.status = self.results_controller.status
            elif self.status == Status.END:
                break
            else:
                print("Unknown status")
        print('End of program')

    def set_menu_controller(self):
        menu_model = MenuModel()
        menu_view = MenuView()
        self.menu_controller = MenuController(menu_model, menu_view)

    def set_game_controller(self):
        game_model = GameModel()
        game_view = GameView()
        self.game_controller = GameController(game_model, game_view)

    def set_results_controller(self):
        results_model = ResultsModel()
        results_view = ResultsView()
        self.results_controller = ResultsController(
            results_model, results_view)
