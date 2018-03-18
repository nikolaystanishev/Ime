import termbox
from textbox import TextBox
import sys

from ui_selectable import Selectable


class Button(TextBox, Selectable):
    def __init__(self, x, y, w, h, text, handler=None,
                 border_color=termbox.WHITE):
        TextBox.__init__(self, x, y, w, h, text, border_color)
        Selectable.__init__(self)
        self.handler = handler

    def on_use(self):
        self.handler()

    def on_select(self):
        self.border_color = termbox.YELLOW

    def on_deselect(self):
        self.border_color = termbox.WHITE
