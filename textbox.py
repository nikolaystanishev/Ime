import termbox
from ui_element import UIElement


class TextBox(UIElement):
    def __init__(self, x, y, w, h, text, border_color=termbox.WHITE):
        super(TextBox, self).__init__(x, y)
        self.w = w
        self.h = h
        self.text = text
        self.border_color = border_color

    def update(self, ms):
        pass

    def draw(self, tb):
        for i in range(0, self.w):
            for j in range(0, self.h):
                if i == 0 or i == self.w - 1 or j == 0 or j == self.h - 1:
                    tb.change_cell(self.x + i, self.y + j, 32, termbox.BLACK,
                                   self.border_color)
                else:
                    x_center = int(self.x + self.w / 2)
                    text_start_x = int(x_center - len(self.text) / 2)
                    text_end_x = int(x_center + len(self.text) / 2)
                    is_in_text_area_x =\
                        i + self.x >= text_start_x and i + self.x < text_end_x
                    y_center = int(self.y + self.h / 2)
                    is_in_text_area_y = j + self.y == y_center
                    if is_in_text_area_x and is_in_text_area_y:
                        tb.change_cell(self.x + i, self.y + j,
                                       ord(self.text[self.x + i - text_start_x]),
                                       termbox.WHITE, termbox.BLACK)
