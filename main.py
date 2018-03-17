import pygame.time
import termbox
from user_input.input_handler import InputHandler
from game_map.game_map import GameMap
from scene_manager import SCENE_MANAGER


# CONSTATN INITIALIZATION
pygame.init()
last_frame_time = 0
tb = termbox.Termbox()
input_handler = InputHandler()
game_map = GameMap('./game_map/game_map.csv')
SCENE_MANAGER['MainMenu'](game_map)


def update(ms):
    current_scene = SCENE_MANAGER['CurrentScene']
    if current_scene is not None:
        current_scene.update(ms)


def draw(tb):
    current_scene = SCENE_MANAGER['CurrentScene']
    if current_scene is not None:
        current_scene.draw(tb)


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
