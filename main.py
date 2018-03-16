import pygame.time
import termbox

pygame.init()
last_frame_time = 0
tb = termbox.Termbox()

def update(ticks):
    return


run_app = True
last_frame_time = pygame.time.get_ticks()
while run_app:
    event_here = tb.poll_event()
    while event_here:
        (type, ch, key, mod, w, h, x, y) = event_here
        if type == termbox.EVENT_KEY:
            #Handle input here
            run_app = False
        event_here = tb.peek_event()
    current_frame_ticks = pygame.time.get_ticks() - last_frame_time
    tb.clear()
    update(current_frame_ticks)
    tb.present()


