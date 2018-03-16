import termbox


class Entity:

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y

        self.symbol = symbol

    def get_coordinates(self):
        return (self.x, self.y)

    def get_symbol(self):
        return self.symbol

    def draw(self, tb):
        fg = termbox.BLACK
        bg = termbox.CYAN

        tb.change_cell(self.x, self.y, self.symbol, fg, bg)


class Player(Entity):

    def __init__(self, x, y):
        symbol = 65
        super().__init__(x, y, symbol)


class Enemy(Entity):

    def __init__(self, x, y):
        symbol = 66
        super().__init__(x, y, symbol)


class Wall(Entity):

    def __init__(self, x, y):
        symbol = 67
        super().__init__(x, y, symbol)


class Treasure(Entity):

    def __init__(self, x, y):
        symbol = 68
        super().__init__(x, y, symbol)


class EndLevel(Entity):

    def __init__(self, x, y):
        symbol = 69
        super().__init__(x, y, symbol)
