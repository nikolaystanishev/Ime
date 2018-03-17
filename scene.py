from game_map.entities import Entity
#from ui import UI

class Scene:
    
    def __init__(self, entities, UI):
        self.entities = entities
        self.UI = UI

    def update(self, ms):
        for entity in entities:
            entity.update(ms)
        if UI not None:
            UI.update(ms)

    def draw(self, tb):
        for entity in entities:
            entity.draw(tb)
        if UI not None:
            UI.draw(tb)

def main_menu():
    pass

def game_scene(game_map):
    SCENE_MANAGER['CurrentScene'] = game_map.load_entities()

def fight_scene():
    pass

SCENE_MANAGER = {'CurrentScene': None,
        'MainMenu': main_menu,
        'GameScene': game_scene,
        'FightScene': fight_scene
        }
