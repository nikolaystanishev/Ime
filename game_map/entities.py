import termbox

from typing import List,Tuple,Set,Dict# perhaps add type annotations
# to at least the tricky operations that return a custom type to help the ide

class Entity:

    def __init__(self, x, y, symbol, items=[], enabled=True):
        self.items = items
        self.x = x
        self.y = y
        self.enabled = enabled
        self.symbol = symbol

    def get_coordinates(self):
        return (self.x, self.y)

    def get_symbol(self):
        return self.symbol

    def get_items(self):
        return self.items

    def draw(self, tb):
        fg = termbox.BLACK
        bg = termbox.CYAN
        tb.change_cell(self.x, self.y, self.symbol, fg, bg)


class Player(Entity):

    def __init__(self, x, y, inventory):
        symbol = 65
        self.last_x = x
        self.last_y = y
        self.inventory = inventory
        super().__init__(x, y, symbol)

    def get_inventory(self):
        return self.inventory

    def get_combat_stats(self):
        return self.inventory.get_combat_stats()

    def change_coordinates(self, event_actions, entities, grid_size):
        new_x = self.x
        new_y = self.y

        if event_actions['MOVE UP']:
            new_y -= 1
        elif event_actions['MOVE DOWN']:
            new_y += 1
        elif event_actions['MOVE RIGHT']:
            new_x += 1
        elif event_actions['MOVE LEFT']:
            new_x -= 1

        if self.is_move_valid(new_x, new_y, grid_size):
            self.last_x = self.x
            self.last_y = self.y
            self.x = new_x
            self.y = new_y

    def return_to_last_pos(self):
        self.x = self.last_x
        self.y = self.last_y

    def is_move_valid(self, new_x, new_y, max_sizes):
        max_y, max_x = max_sizes
        return (not (new_x < 0 or new_y < 0 or new_x >= max_x or new_y >= max_y))

    def check_collision(self, entities):
        for entity in entities:
            if entity.x == self.x and self.y == entity.y and entity.enabled:
                # Check Entity type for Enemy
                if type(entity) is Treasure:
                    self.inventory.take_item(entity)
                    return True
                return False
        return True



class Enemy(Entity):

    def __init__(self, x, y):
        symbol = 66
        super().__init__(x, y, symbol)


class Wall(Entity):

    def __init__(self, x, y):
        symbol = 67
        super().__init__(x, y, symbol)


class Treasure(Entity):

    def __init__(self, x, y, items=[]):
        symbol = 68
        super().__init__(x, y, symbol, items)


class EndLevel(Entity):

    def __init__(self, x, y):
        symbol = 69
        super().__init__(x, y, symbol)
