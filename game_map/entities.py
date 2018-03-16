import termbox


class Entity:

    def __init__(self, x, y, symbol, items=[], alive=True):
        self.items = items
        self.x = x
        self.y = y
        self.alive = alive
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
        if self.alive:
            tb.change_cell(self.x, self.y, self.symbol, fg, bg)


class Player(Entity):

    def __init__(self, x, y, inventory):
        symbol = 65
        self.inventory = inventory
        super().__init__(x, y, symbol)

    def get_inventory(self):
        return self.inventory

    def get_combat_stats(self):
        return self.inventory.get_combat_stats()


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


class Empty(Entity):

    def __init__(self, x, y):
        symbol = 0
        super().__init__(x, y, symbol)
