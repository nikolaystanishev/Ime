from button import Button
from scene import Scene
from box import Box
from ui import UI

def main_menu(game_map):
    button1 = Button(0, 0, 20, 8, "Start",
                     lambda: SCENE_MANAGER['GameScene'](game_map))
    button2 = Button(0, 10, 20, 8, "Exit")

    ui_elements = []

    ui_elements.append(button1)
    ui_elements.append(button2)

    button1.set_next_selectable(button2)
    button2.set_next_selectable(button1)
    button1.set_prev_selectable(button2)
    button2.set_prev_selectable(button1)

    ui = UI(ui_elements)
    ui.set_current_selectable(button1)

    SCENE_MANAGER['CurrentScene'] = Scene([], ui)


def game_scene(game_map):
    SCENE_MANAGER['CurrentScene'] = Scene(game_map.load_entities(), None)


def fight_scene():
    playerUIBox = Box(5, 2, 20, 30)
    enemyUIBox = Box(45, 2, 20, 30)
    playerAttackButton = Button(8, 4, 14, 5, "Attack",
                                lambda: FIGHT_MANAGER['Attack']())
    playerDefendButton = Button(8, 10, 14, 5, "Defend",
                                lambda: FIGHT_MANAGER['Defend']())

    ui_elements = []
    ui_elements.append(playerUIBox)
    ui_elements.append(enemyUIBox)
    ui_elements.append(playerAttackButton)
    ui_elements.append(playerDefendButton)
    ui = UI(ui_elements)
    
    playerAttackButton.set_next_selectable(playerDefendButton)
    playerDefendButton.set_next_selectable(playerAttackButton)
    playerAttackButton.set_prev_selectable(playerDefendButton)
    playerDefendButton.set_prev_selectable(playerAttackButton)
    ui.set_current_selectable(playerAttackButton)

    SCENE_MANAGER['CurrentScene'] = Scene([], ui)
    pass

SCENE_MANAGER = {'CurrentScene': None,
                 'OldScene': None,
                 'MainMenu': main_menu,
                 'GameScene': game_scene,
                 'FightScene': fight_scene}
