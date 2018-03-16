import numpy as np
import pandas as pd

from entities import Player, Enemy, Wall, Treasure, EndLevel, Empty


class GameMap:

    def __init__(self, game_map_file):
        self.entities = self.create_entities(game_map_file)

    def create_entities(self, game_map_file):
        grid = self.create_grid(game_map_file)
        grid_size = grid.shape

        entities = []

        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                if grid[row][col] == 0:
                    entitie = Empty(row, col)
                elif grid[row][col] == 1:
                    entitie = Player(row, col)
                elif grid[row][col] == 2:
                    entitie = Enemy(row, col)
                elif grid[row][col] == 3:
                    entitie = Wall(row, col)
                elif grid[row][col] == 4:
                    entitie = Treasure(row, col)
                elif grid[row][col] == 5:
                    entitie = EndLevel(row, col)

                entities.append(entitie)

        return entities

    def create_grid(self, game_map_file):
        grid = pd.read_csv(game_map_file, header=None, skiprows=1)
        grid = np.array(grid)

        return grid

    def get_entities(self):
        return self.entities


if __name__ == '__main__':
    gm = GameMap("./game_map/game_map.csv")
    print(gm.get_entities())
