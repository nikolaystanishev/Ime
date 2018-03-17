from game_map.entities import Entity, Player
from ui import UI
from textbox import TextBox
from button import Button
#from ui import UI

class Scene:
    
    def __init__(self, entities, UI):
        self.entities = entities
        self.UI = UI

    def update(self, ms):
        for entity in self.entities:
            if type(entity) == Player:
                entity.update(ms)
                entity.handle_collision(self.entities)
            else:
                entity.update(ms)
        if self.UI is not None:
            self.UI.update(ms)

    def draw(self, tb):
        for entity in self.entities:
            entity.draw(tb)
        if self.UI is not None:
            self.UI.draw(tb)

def main_menu():
    pass

def game_scene(game_map):
    # textbox1 = TextBox(0, 0, 20, 10, "testing")
    button1 = Button(0, 6, 20, 10, "button1")
    button2 = Button(0, 17, 20, 10, "button2")
    ui_elements = []
    # ui_elements.append(textbox1)
    ui_elements.append(button1)
    ui_elements.append(button2)
    button1.set_next_selectable(button2)
    button2.set_next_selectable(button1)
    button1.set_prev_selectable(button2)
    button2.set_prev_selectable(button1)

    ui = UI(ui_elements)
    ui.set_current_selectable(button1)
    SCENE_MANAGER['CurrentScene'] = Scene(game_map.load_entities(), ui)

def fight_scene():
    pass

SCENE_MANAGER = {'CurrentScene': None,
        'MainMenu': main_menu,
        'GameScene': game_scene,
        'FightScene': fight_scene
        }
