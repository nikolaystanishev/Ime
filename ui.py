from user_input.events import MAP_EVENT_ACTIONS
class UI:
    
    def __init__(self, elements):
        self.elements = elements
        self.current_selectable = None
        pass

    def update(self, ms):
        if MAP_EVENT_ACTIONS['USE'] == True:
            on_use_press()
        for e in elements:
            e.update(ms)

    def draw(self, tb):
        for e in elements:
            e.draw(tb)

    def set_current_selectable(self, selectable):
        if type(selectable) is Selectable:
            if self.current_selectable is not None:
                self.current_selectable.on_deselect()
            self.current_selectable = selectable
            self.current_selectable.on_select()

    def next_selectable(self):
        new_selectable = self.current_selectable.get_next_selectable()
        set_current_selectable(new_selectable)

    def prev_selectable(self):
        new_selectable = self.current_selectable.get_prev_selectable()
        set_current_selectable(new_selectable)

    def on_use_press(self):
        self.current_selectable.on_use()
