import numpy as np
import pandas as pd
import termbox

from Inventory import Inventory
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
                entity = None

                if grid[row][col] == 1:
                    entity = Player(col, row, Inventory())
                    self.player = entity
                    continue
                elif grid[row][col] == 2:
                    entity = Enemy(col, row)
                elif grid[row][col] == 3:
                    entity = Wall(col, row)
                elif grid[row][col] == 4:
                    entity = Treasure(col, row)
                elif grid[row][col] == 5:
                    entity = EndLevel(col, row)

                if entity:
                    entities.append(entity)

        return entities

    def create_grid(self, game_map_file):
        grid = pd.read_csv(game_map_file, header=None, skiprows=1)
        grid = np.array(grid)

        return grid

    def get_entities(self):
        return self.entities

    def draw_map(self, tb):
        for entity in self.entities:
            if entity.enabled:
                entity.draw(tb)

        self.player.draw(tb)

    def move_player(self, tb, event_actions):
        self.player.change_coordinates(event_actions, self.entities,
                                       self.grid_size)

    def get_player(self):
        return self.player


if __name__ == '__main__':
    gm = GameMap("./game_map/game_map.csv")

    with termbox.Termbox() as tb:
        while True:
            tb.clear()
            gm.draw_map(tb)
            tb.present()
