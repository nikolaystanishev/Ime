from abc import abstractmethod

class UIElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def update(self, ms):
        pass

    @abstractmethod
    def draw(self, tb):
        pass


    
