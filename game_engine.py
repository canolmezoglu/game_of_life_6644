# game_engine.py
import numpy as np

ON = 255
OFF = 0

def create_grid(N):
    return np.zeros((N, N), dtype=int)

def update_grid(grid):
    N = grid.shape[0]
    padded_grid = np.pad(grid, 1, mode='wrap')
    neighbor_sum = (
        padded_grid[:-2, :-2] + padded_grid[:-2, 1:-1] + padded_grid[:-2, 2:] +
        padded_grid[1:-1, :-2] + padded_grid[1:-1, 2:] +
        padded_grid[2:, :-2] + padded_grid[2:, 1:-1] + padded_grid[2:, 2:]
    ) // ON

    alive = grid == ON
    dead = grid == OFF
    underpopulation = neighbor_sum < 2
    overpopulation = neighbor_sum > 3
    reproduction = neighbor_sum == 3

    new_grid = grid.copy()
    new_grid[alive & (underpopulation | overpopulation)] = OFF
    new_grid[dead & reproduction] = ON

    return new_grid