import pygame.time
import termbox
from user_input.input_handler import InputHandler
from user_input.events import EVENT_ACTIONS
from game_map.game_map import GameMap


# CONSTATN INITIALIZATION
pygame.init()
last_frame_time = 0
tb = termbox.Termbox()
input_handler = InputHandler()
game_map = GameMap('./game_map/game_map.csv')
tb.clear()
game_map.draw_map(tb)
tb.present()


def update(ticks):
    game_map.move_player(tb, EVENT_ACTIONS)
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
            # run_app = False
        event_here = tb.peek_event()
    current_frame_ticks = pygame.time.get_ticks() - last_frame_time
    tb.clear()
    update(current_frame_ticks)
    tb.present()

tb.close()
