import abc


class ModelInterface(abc.ABC):
    @abc.abstractmethod
    def handle_event(self, event):
        pass

    @abc.abstractmethod
    def get_game_state(self):
        pass
