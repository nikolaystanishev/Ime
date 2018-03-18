import termbox
from ui_element import UIElement


class Box(UIElement):
    def __init__(self, x, y, w, h, border_color=termbox.WHITE):
        super(Box, self).__init__(x, y)
        self.w = w
        self.h = h
        self.border_color = border_color

    def update(self, ms):
        pass

    def draw(self, tb):
        for i in range(0, self.w):
            for j in range(0, self.h):
                if i == 0 or i == self.w - 1 or j == 0 or j == self.h - 1:
                    tb.change_cell(self.x + i, self.y + j, 32, termbox.BLACK,
                                   self.border_color)
