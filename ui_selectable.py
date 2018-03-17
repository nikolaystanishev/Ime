from abc import abstractmethod


class Selectable():
    def __init__(self):
        self.next_selectable = None
        self.prev_selectable = None

    def get_next_selectable(self):
        return self.next_selectable

    def get_prev_selectable(self):
        return self.prev_selectable

    def set_next_selectable(self, selectable):
        if Selectable in type(selectable).__bases__:
            self.next_selectable = selectable

    def set_prev_selectable(self, selectable):
        if Selectable in type(selectable).__bases__:
            self.prev_selectable = selectable

    @abstractmethod
    def on_use(self):
        pass

    @abstractmethod
    def on_select(self):
        pass

    @abstractmethod
    def on_deselect(self):
        pass
