import pygame.time
import termbox
from user_input.input_handler import InputHandler
from Item import DamageItem
from game_map.game_map import GameMap
from scene_manager import SCENE_MANAGER
from game_state_manager import GAME_STATE_MANAGER, GameState
from fight_manager import FIGHT_MANAGER

# from Inventory import Inventory

# CONSTATN INITIALIZATION
pygame.init()
last_frame_time = 0
tb = termbox.Termbox()
input_handler = InputHandler()
game_map = GameMap('./game_map/game_map.csv')
SCENE_MANAGER['MainMenu'](game_map)
# inventory = Inventory(5, 10)
# inventory.add_item(DamageItem(500))
#SCENE_MANAGER['FightScene'](inventory)

current_game_state = GAME_STATE_MANAGER['CurrentState']

def update_fight():
    if FIGHT_MANAGER['CurrentFight'].is_battle_over() == True:
        if FIGHT_MANAGER['CurrentFight'].get_player_inventory().get_health() > 0:
            FIGHT_MANAGER['CurrentFight'] = None
            GAME_STATE_MANAGER['CurrentSate'] = GameState.MAP
            SCENE_MANAGER['CurrentScene'] = SCENE_MANAGER['OldScene']
        else:
            FIGHT_MANAGER['CurrentFight'] = None
            GAME_STATE_MANAGER['CurrentSate'] = GameState.MAIN
            global game_map
            SCENE_MANAGER['MainMenu'](game_map)
        return
    if FIGHT_MANAGER['IsPlayerTurn'] == False:
        FIGHT_MANAGER['AITurn']()

def update(ms):
    global current_game_state
    if current_game_state != GAME_STATE_MANAGER['CurrentState']:
        if GAME_STATE_MANAGER['CurrentState'] == GameState.IN_FIGHT:
            SCENE_MANAGER['FightScene']()

    current_game_state = GAME_STATE_MANAGER['CurrentState'] 
    current_scene = SCENE_MANAGER['CurrentScene']
    if current_scene is not None:
        current_scene.update(ms)
    if GAME_STATE_MANAGER['CurrentState'] == GameState.IN_FIGHT:
        update_fight()


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
