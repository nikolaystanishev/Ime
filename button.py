import termbox
from textbox import TextBox
from ui_selectable import Selectable

class Button(TextBox, Selectable):
    def __init__(self, x, y, w, h, text, border_color=termbox.WHITE):
        TextBox.__init__(x, y, w, h, text, border_color)
        Selectable.__init()

    def on_use():
        print("used")

    def on_select():
        pass

    def on_deselect():
        pass
