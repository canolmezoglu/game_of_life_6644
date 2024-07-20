# pattern_generator.py
import numpy as np

ON = 255
OFF = 0

def random_grid(N, p_alive=0.2):
    return np.random.choice([ON, OFF], N * N, p=[p_alive, 1-p_alive]).reshape(N, N)

def figure_eight(N):
    figure_eight_size = max(6, N // 10)
    if figure_eight_size % 2 != 0:
        figure_eight_size -= 1

    figure_eight = np.zeros((figure_eight_size, figure_eight_size), dtype=int)
    center = figure_eight_size // 2
    figure_eight[:center, :center] = 1
    figure_eight[center:, center:] = 1

    grid = np.zeros((N, N), dtype=int)
    start = (N - figure_eight_size) // 2
    grid[start:start + figure_eight_size, start:start + figure_eight_size] = figure_eight

    return grid * ON

import numpy as np

def block(N):
    """Still life: Block"""
    pattern = np.zeros((N, N), dtype=int)
    center = N // 2
    pattern[center-1:center+1, center-1:center+1] = 255
    return pattern

def blinker(N):
    """Oscillator: Blinker"""
    pattern = np.zeros((N, N), dtype=int)
    center = N // 2
    pattern[center, center-1:center+2] = 255
    return pattern

def glider(N):
    """Spaceship: Glider"""
    pattern = np.zeros((N, N), dtype=int)
    glider = np.array([[0, 255, 0],
                       [0, 0, 255],
                       [255, 255, 255]])
    start = N // 2 - 1
    pattern[start:start+3, start:start+3] = glider
    return pattern

def pulsar(N):
    """Oscillator: Pulsar (period 3)"""
    pattern = np.zeros((N, N), dtype=int)
    pulsar = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    start = (N - pulsar.shape[0]) // 2
    pattern[start:start+pulsar.shape[0], start:start+pulsar.shape[1]] = pulsar * 255
    return pattern




def gosper_glider_gun(N):
    """Pattern: Gosper Glider Gun"""
    pattern = np.zeros((N, N), dtype=int)
    gun = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ])
    start_row = (N - gun.shape[0]) // 2
    start_col = (N - gun.shape[1]) // 2
    pattern[start_row:start_row+gun.shape[0], start_col:start_col+gun.shape[1]] = gun * 255
    return pattern