import pygame.time
import termbox
from ui import UI
from textbox import TextBox

pygame.init()
last_frame_time = 0
tb = termbox.Termbox()

def update(ticks):
    return


run_app = True
last_frame_time = pygame.time.get_ticks()
test1 = TextBox(0, 0, 10, 10, "test")
test2 = TextBox(20, 5, 20, 5, "test")
while run_app:
    tb.clear()
    event_here = tb.peek_event()
    while event_here:
        (type, ch, key, mod, w, h, x, y) = event_here
        if type == termbox.EVENT_KEY:
            #Handle input here
            run_app = False
        event_here = tb.peek_event()
    current_frame_ticks = pygame.time.get_ticks() - last_frame_time
    test1.draw(tb)
    test2.draw(tb)
    update(current_frame_ticks)
    tb.present()


