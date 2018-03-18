from FightingMechanics import Fight, BattleAction
from game_state_manager import GAME_STATE_MANAGER

def new_fight(player, enemy):
    FIGHT_MANAGER['CurrentFight'] = Fight(player.get_inventory(), enemy.get_inventory())
    GAME_STATE_MANAGER['StartFight']()

def end_fight(player, enemy):
    FIGHT_MANAGER['CurrentFight'] = None
    if player.get_inventory().get_health() <= 0:
        pass
    else:
        pass

def handle_attack_button_press():
    if FIGHT_MANAGER['IsPlayerTurn'] == True:
        FIGHT_MANAGER['CurrentFight'].execute_player_action(BattleAction.ATTACK)
        FIGHT_MANAGER['IsPlayerTurn'] = False

def handle_defend_button_press():
    if FIGHT_MANAGER['IsPlayerTurn'] == True:
        FIGHT_MANAGER['CurrentFight'].execute_player_action(BattleAction.DEFEND)
        FIGHT_MANAGER['IsPlayerTurn'] = False

def handle_item_use(item_id):
    print("test")
    if FIGHT_MANAGER['IsPlayerTurn'] == True:
        FIGHT_MANAGER['CurrentFight'].execute_use(item_id)
        FIGHT_MANAGER['IsPlayerTurn'] = False

def ai_turn():
    if FIGHT_MANAGER['IsPlayerTurn'] == False:
        FIGHT_MANAGER['CurrentFight'].execute_enemy_action(item_id)
        FIGHT_MANAGER['IsPlayerTurn'] = True


FIGHT_MANAGER = {'CurrentFight': None,
                 'IsPlayerTurn': True,
                 'Attack': handle_attack_button_press,
                 'Defend': handle_defend_button_press,
                 'Use': handle_item_use,
                 'AITurn': ai_turn,
                 'NewFight': new_fight}
