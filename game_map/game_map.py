import numpy as np
import pandas as pd
import termbox


from game_map.entities import Player, Enemy, Wall, Treasure, EndLevel


class GameMap:

    def __init__(self, game_map_file):
        self.player = None
        self.grid_size = None
        self.entities = self.create_entities(game_map_file)

    def create_entities(self, game_map_file):
        grid = self.create_grid(game_map_file)
        self.grid_size = grid.shape

        entities = []

        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                entitie = None

                if grid[row][col] == 1:
                    entitie = Player(col, row)
                    self.player = entitie
                    continue
                elif grid[row][col] == 2:
                    entitie = Enemy(col, row)
                elif grid[row][col] == 3:
                    entitie = Wall(col, row)
                elif grid[row][col] == 4:
                    entitie = Treasure(col, row)
                elif grid[row][col] == 5:
                    entitie = EndLevel(col, row)

                if entitie:
                    entities.append(entitie)

        return entities

    def create_grid(self, game_map_file):
        grid = pd.read_csv(game_map_file, header=None, skiprows=1)
        grid = np.array(grid)

        return grid

    def get_entities(self):
        return self.entities

    def draw_map(self, tb):
        for entitie in self.entities:
            entitie.draw(tb)

        self.player.draw(tb)

    def move_player(self, tb, event_actions):
        self.player.change_coordinates(event_actions, self.entities,
                                       self.grid_size)

        self.draw_map(tb)


if __name__ == '__main__':
    gm = GameMap("./game_map/game_map.csv")

    with termbox.Termbox() as tb:
        while True:
            tb.clear()
            gm.draw_map(tb)
            tb.present()
