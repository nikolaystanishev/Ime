class Entity:

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y

        self.symbol = symbol


class Player(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)


class Enemy(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)


class Wall(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)


class Treasure(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)


class EndLevel(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)


class Empty(Entity):

    def __init__(self, x, y):
        symbol = None
        super().__init__(x, y, symbol)
