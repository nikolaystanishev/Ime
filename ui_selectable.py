from ui_element import UIElement
from abc import abstractmethod

class Selectable():
    def __init__(self):
        self.next_selectable = None
        self.prev_selectable = None
    
    def get_next_selectable(self):
        return self.next_selectable

    def get_prev_selectable(self):
        return self.prev_selectable

    @abstractmethod
    def on_use(self):
        pass

    @abstractmethod
    def on_select(self):
        pass

    @abstractmethod
    def on_deselect(self):
        pass
