import termbox

from user_input.events import MAP_EVENT_ACTIONS
from typing import List,Tuple,Set,Dict# perhaps add type annotations
from fight_manager import FIGHT_MANAGER
from game_state_manager import GAME_STATE_MANAGER, GameState
# to at least the tricky operations that return a custom type to help the ide

class Entity:

    def __init__(self, x, y, symbol, enabled=True):
        self.x = x
        self.y = y
        self.enabled = enabled
        self.symbol = symbol

    def get_position(self):
        return (self.x, self.y)

    def get_symbol(self):
        return self.symbol

    def get_items(self):
        return self.items

    def update(self, ms):
        return

    def draw(self, tb):
        if not self.enabled:
            return
        fg = termbox.BLACK
        bg = termbox.CYAN
        tb.change_cell(self.x, self.y, self.symbol, fg, bg)

class FightableEntity(Entity):

    def __init__(self, x, y, inventory, symbol):
        self.inventory = inventory
        super().__init__(x, y, symbol)


    def get_inventory(self):
        return self.inventory


    def get_combat_stats(self):
        return self.inventory.get_combat_stats()


class Player(FightableEntity):

    def __init__(self, x, y, inventory):
        symbol = ord('☺')
        self.last_x = x
        self.last_y = y
        self.inventory = inventory
        super().__init__(x, y, inventory, symbol)


    def update(self, ms):
        if GAME_STATE_MANAGER['CurrentState'] != GameState.MAP:
            return
        new_x = self.x
        new_y = self.y
        has_new = False

        if MAP_EVENT_ACTIONS['MOVE UP']:
            new_y -= 1
            has_new = True
        elif MAP_EVENT_ACTIONS['MOVE DOWN']:
            new_y += 1
            has_new = True
        elif MAP_EVENT_ACTIONS['MOVE RIGHT']:
            new_x += 1
            has_new = True
        elif MAP_EVENT_ACTIONS['MOVE LEFT']:
            new_x -= 1
            has_new = True

        if has_new:
            self.last_x = self.x
            self.last_y = self.y

        self.x = new_x
        self.y = new_y
        


    def return_to_last_pos(self):
        self.x = self.last_x
        self.y = self.last_y

    def on_collision(self, entity):
        # Check Entity type for Enemy
        if type(entity) is Enemy:
            FIGHT_MANAGER['NewFight'](self, entity)
            entity.enabled = False
        if type(entity) is Treasure:
            self.inventory.take_item(entity)

    def handle_collision(self, entities):
        is_colliding = False
        for entity in entities:
            if entity == self:
                continue
            if entity.x == self.x and self.y == entity.y and entity.enabled:
                self.on_collision(entity)
                is_colliding = True
        if is_colliding:
            self.return_to_last_pos()
    

class Enemy(FightableEntity):

    def __init__(self, x, y, inventory):
        symbol = ord('☠')
        super().__init__(x, y, inventory, symbol)



class Wall(Entity):

    def __init__(self, x, y):
        symbol = 0
        super().__init__(x, y, symbol)


class Treasure(Entity):

    def __init__(self, x, y, items=[]):
        symbol = ord('⚛')
        super().__init__(x, y, symbol)
        self.items=items


class EndLevel(Entity):

    def __init__(self, x, y):
        symbol = 69
        super().__init__(x, y, symbol)
