import termbox
from ui_element import UIElement

class TextBox(UIElement):
    def __init__(self, x, y, w, h, text, borderSym=219):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.text = text
        self.borderSym = borderSym

    def update(ms):
        pass

    def draw(tb):
        for i in range(0, w):
            for j in range(0, h):
                tb.change_cell(i, j, self.borderSym, termbox.BLACK, termbox.CYAN);
