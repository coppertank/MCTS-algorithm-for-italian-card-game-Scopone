from abc import ABC, abstractmethod


class ViewInterface(ABC):
    @abstractmethod
    def draw(self):
        pass
