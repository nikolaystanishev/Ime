import numpy as np
import pandas as pd


class GameMap:

    def __init__(self, game_map_file):
        self.grid = self.create_grid(game_map_file)
        self.grid_size = self.grid.shape

    def create_grid(self, game_map_file):
        grid = pd.read_csv(game_map_file, header=None, skiprows=1)
        grid = np.array(grid)

        return grid


if __name__ == '__main__':
    gm = GameMap("./game_map.csv")
