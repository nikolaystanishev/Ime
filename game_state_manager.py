from enum import Enum

class GameState(Enum):
    MAIN=0
    MAP=1
    IN_FIGHT=2

def on_enter_map():
    GAME_STATE_MANAGER['CurrentState'] = GameState.MAP

def on_fight_start():
    GAME_STATE_MANAGER['CurrentState'] = GameState.IN_FIGHT

def on_return_to_main():
    GAME_STATE_MANAGER['CurrentState'] = GameState.MAIN

GAME_STATE_MANAGER = {'CurrentState': GameState.MAIN,
                      'EnterMap': on_enter_map,
                      'StartFight':on_fight_start,
                      'ReturnTomain':on_return_to_main}
