from button import Button
from scene import Scene
from box import Box
from ui import UI
from fight_manager import FIGHT_MANAGER

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


def fight_scene(player_inventory):
    player_ui_box = Box(5, 2, 40, 30)
    enemy_ui_box = Box(55, 2, 40, 30)
    player_attack_button = Button(10, 4, 30, 5, "Attack",
                                lambda: FIGHT_MANAGER['Attack']())
    player_defend_button = Button(10, 10, 30, 5, "Defend",
                                lambda: FIGHT_MANAGER['Defend']())

    player_attack_button.set_next_selectable(player_defend_button)
    player_defend_button.set_next_selectable(player_attack_button)
    player_attack_button.set_prev_selectable(player_defend_button)
    player_defend_button.set_prev_selectable(player_attack_button)

    use_buttons = []
    i = 0
    items = player_inventory.get_items()
    for j in range(0, len(items)):
        item = items[j]
        new_button = Button(10, 16 + 6*i, 30, 5, str(item),
                            lambda: FIGHT_MANAGER['Use'](j))
        use_buttons.append(new_button)
    for j in range(0, len(use_buttons)):
        button = use_buttons[j]
        if j == 0:
            button.set_prev_selectable(player_defend_button)
            player_defend_button.set_next_selectable(button)
        else:
            button.set_prev_selectable(use_buttons[j-1])
        if j == len(use_buttons) - 1:
            button.set_next_selectable(player_attack_button)
            player_attack_button.set_prev_selectable(button)
        else:
            button.set_next_selectable(use_buttons[j+1])

    ui_elements = []
    ui_elements.append(player_ui_box)
    ui_elements.append(enemy_ui_box)
    ui_elements.append(player_attack_button)
    ui_elements.append(player_defend_button)
    ui_elements += use_buttons
    ui = UI(ui_elements)
    
    ui.set_current_selectable(player_attack_button)

    SCENE_MANAGER['CurrentScene'] = Scene([], ui)
    pass

SCENE_MANAGER = {'CurrentScene': None,
                 'OldScene': None,
                 'MainMenu': main_menu,
                 'GameScene': game_scene,
                 'FightScene': fight_scene}
