import termbox
from events import EVENT_ACTIONS


class InputHandler(object):
    def __init__(self):
        self.addressable_btns = {
            'w': 'MOVE UP',
            'a': 'MOVE LEFT',
            's': 'MOVE DOWN',
            'd': 'MOVE RIGHT',
            termbox.KEY_ENTER: 'USE',
            termbox.KEY_ARROW_UP: 'MOVE UP',
            termbox.KEY_ARROW_DOWN: 'MOVE DOWN',
            termbox.KEY_ARROW_LEFT: 'MOVE LEFT',
            termbox.KEY_ARROW_RIGHT: 'MOVE RIGHT'
        }

    def update(self, event):
        type, ch, key, mod, w, h, x, y = event
        key = key if key != 0 else ch
        if key in self.addressable_btns.keys():
            EVENT_ACTIONS[self.addressable_btns[key]] = True

    def reset_events(self):
        for k, _ in EVENT_ACTIONS.items():
            EVENT_ACTIONS[k] = False

    def is_event_alive(self, event_name):
        return EVENT_ACTIONS[event_name]
