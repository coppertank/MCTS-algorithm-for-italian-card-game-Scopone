from abc import ABC, abstractmethod


class ControllerInterface(ABC):
    @abstractmethod
    def run(self):
        pass
