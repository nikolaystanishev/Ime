import pygame.time
import termbox
from user_input.input_handler import InputHandler
from user_input.events import MAP_EVENT_ACTIONS
from game_map.game_map import GameMap
from game_map.entities import Player


# CONSTATN INITIALIZATION
pygame.init()
last_frame_time = 0
tb = termbox.Termbox()
input_handler = InputHandler()
game_map = GameMap('./game_map/game_map.csv')


def update(ms):
    for entity in entities:
        # print(type(entity))
        if type(entity) == Player:
            entity.update(ms, MAP_EVENT_ACTIONS)
            entity.handle_collision(entities)
        else:
            entity.update(ms)


def draw(tb):
    for entity in entities:
        if entity.enabled:
            entity.draw(tb)


run_app = True
last_frame_time = pygame.time.get_ticks()

entities = game_map.load_entities()

while run_app:
    input_handler.reset_events()
    event = tb.peek_event()
    while event:
        (event_type, ch, key, mod, w, h, x, y) = event
        if event_type == termbox.EVENT_KEY:
            input_handler.update(event)
            # run_app = False
        event = tb.peek_event()
    current_frame_ticks = pygame.time.get_ticks() - last_frame_time
    last_frame_time = pygame.time.get_ticks()
    tb.clear()
    update(current_frame_ticks)
    draw(tb)
    tb.present()

tb.close()
