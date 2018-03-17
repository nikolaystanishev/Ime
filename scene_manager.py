from button import Button
from scene import Scene
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
    pass


SCENE_MANAGER = {'CurrentScene': None,
                 'MainMenu': main_menu,
                 'GameScene': game_scene,
                 'FightScene': fight_scene}
