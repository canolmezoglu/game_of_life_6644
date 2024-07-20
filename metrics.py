# metrics_tracker.py
import time
import numpy as np


class GameOfLifeMetrics:
    def __init__(self):
        self.start_time = time.time()
        self.iterations = 0
        self.live_cell_counts = []
        self.live_cell_percentages = []

    def tag_iteration(self, grid):
        self.iterations += 1
        live_cells = np.sum(grid == 255)
        total_cells = grid.size

        self.live_cell_counts.append(live_cells)
        self.live_cell_percentages.append((live_cells / total_cells) * 100)

    def print_metrics(self):
        end_time = time.time()
        execution_time = end_time - self.start_time

        print(f"Game of Life Simulation Metrics:")
        print(f"Total iterations: {self.iterations}")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Initial live cells: {self.live_cell_counts[0]}")
        print(f"Final live cells: {self.live_cell_counts[-1]}")
        print(f"Initial live cell percentage: {self.live_cell_percentages[0]:.2f}%")
        print(f"Final live cell percentage: {self.live_cell_percentages[-1]:.2f}%")
        print(f"Average live cells: {np.mean(self.live_cell_counts):.2f}")
        print(f"Average live cell percentage: {np.mean(self.live_cell_percentages):.2f}%")

    def get_metrics_dict(self):
        return {
            'iterations': self.iterations,
            'execution_time': time.time() - self.start_time,
            'live_cell_counts': self.live_cell_counts,
            'live_cell_percentages': self.live_cell_percentages
        }