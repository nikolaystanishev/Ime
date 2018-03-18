import numpy as np
import pandas as pd
import termbox

from Inventory import Inventory
from Item import DamageItem
from game_map.entities import Player, Enemy, Wall, Treasure, EndLevel


class GameMap:

    def __init__(self, game_map_file):
        self.player = None
        self.grid_size = None
        self.map_file = game_map_file

    def load_entities(self):
        grid = self.create_grid(self.map_file)

        entities = []

        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                entity = None

                if grid[row][col] == 1:
                    entity = Player(col, row, Inventory(2, 10))
                elif grid[row][col] == 2:
                    inventory = Inventory(3, 5)
                    inventory.add_item(DamageItem())
                    entity = Enemy(col, row, inventory)
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


if __name__ == '__main__':
    gm = GameMap("./game_map/game_map.csv")

    with termbox.Termbox() as tb:
        while True:
            tb.clear()
            gm.draw_map(tb)
            tb.present()
