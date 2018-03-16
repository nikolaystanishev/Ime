import pygame.time
import termbox
from InputHandler import InputHandler
from events import EVENT_ACTIONS


# CONSTATN INITIALIZATION
pygame.init()
last_frame_time = 0
tb = termbox.Termbox()
input_handler = InputHandler()


def update(ticks):
    # input_handler.update()
    return


run_app = True
last_frame_time = pygame.time.get_ticks()

while run_app:
    input_handler.reset_events()
    event_here = tb.poll_event()
    while event_here:
        (type, ch, key, mod, w, h, x, y) = event_here
        if type == termbox.EVENT_KEY:
            input_handler.update(event_here)
            run_app = False
        event_here = tb.peek_event()
    current_frame_ticks = pygame.time.get_ticks() - last_frame_time
    tb.clear()
    update(current_frame_ticks)
    tb.present()

tb.close()
