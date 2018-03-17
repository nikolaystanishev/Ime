from game_map.entities import Entity, Player
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
    SCENE_MANAGER['CurrentScene'] = Scene(game_map.load_entities(), None)

def fight_scene():
    pass

SCENE_MANAGER = {'CurrentScene': None,
        'MainMenu': main_menu,
        'GameScene': game_scene,
        'FightScene': fight_scene
        }
