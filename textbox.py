import termbox
from ui_element import UIElement

class TextBox(UIElement):
    def __init__(self, x, y, w, h, text, border_sym=termbox.WHITE):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.text = text
        self.border_sym = border_sym

    def update(self, ms):
        pass

    def draw(self, tb):
        for i in range(0, self.w):
            for j in range(0, self.h):
                if i == 0 or i == self.w - 1 or j == 0 or j == self.h -1:
                    tb.change_cell(self.x + i, self.y + j, 32, termbox.BLACK, self.border_sym);
                else:
                    x_center = self.x + self.w/2
                    text_start_x = int(x_center - len(self.text)/2)
                    text_end_x = int(x_center + len(self.text)/2)
                    is_in_text_area_x = i >= text_start_x  and i < text_end_x
                    y_center = self.y + self.h/2
                    is_in_text_area_y = j == y_center-1
                    if is_in_text_area_x and is_in_text_area_y:
                        tb.change_cell(self.x + i, self.y + j, ord(self.text[i-text_start_x]), termbox.WHITE, termbox.BLACK)

                    
