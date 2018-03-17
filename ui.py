from user_input.events import MAP_EVENT_ACTIONS
from ui_selectable import Selectable


class UI:

    def __init__(self, elements):
        self.elements = elements
        self.current_selectable = None
        pass

    def update(self, ms):
        if MAP_EVENT_ACTIONS['USE']:
            self.on_use_press()
        if MAP_EVENT_ACTIONS['MOVE UP'] or MAP_EVENT_ACTIONS['MOVE DOWN']:
            self.next_selectable()
        for e in self.elements:
            e.update(ms)

    def draw(self, tb):
        for e in self.elements:
            e.draw(tb)

    def set_current_selectable(self, selectable):
        if Selectable in type(selectable).__bases__:
            if self.current_selectable is not None:
                self.current_selectable.on_deselect()
            self.current_selectable = selectable
            self.current_selectable.on_select()

    def next_selectable(self):
        if self.current_selectable is not None:
            new_selectable = self.current_selectable.get_next_selectable()
            self.set_current_selectable(new_selectable)

    def prev_selectable(self):
        if self.current_selectable is not None:
            new_selectable = self.current_selectable.get_prev_selectable()
            self.set_current_selectable(new_selectable)

    def on_use_press(self):
        if self.current_selectable is not None:
            self.current_selectable.on_use()
