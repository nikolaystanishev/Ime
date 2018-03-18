import termbox
from ui_element import UIElement;

class HPDisplay(UIElement):
    
    def __init__(self, x, y, text, inventory):
        self.text = text
        self.inventory = inventory
        super().__init__(x, y),
        
    def draw(self, tb):
        text_length = len(self.text)
        for i in range(0, text_length):
            ascii_code = ord(self.text[i])
            tb.change_cell(self.x + i, self.y, ascii_code, termbox.WHITE, termbox.BLACK)

        health = str(self.inventory.get_health())
        for i in range(0, len(health)):
            ascii_code = ord(health[i])
            tb.change_cell(self.x + i + text_length, self.y, ascii_code, termbox.WHITE, termbox.BLACK)
