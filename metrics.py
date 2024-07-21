import time
import numpy as np

class GameOfLifeMetrics:
    def __init__(self):
        self.start_time = time.time()
        self.iterations = 0
        self.live_cell_counts = []
        self.live_cell_percentages = []
        self.birth_rate = []
        self.survival_rate = []
        self.previous_grid = None
        self.stabilized = False
        self.stabilization_time = None
        self.max_live_cells = 0
        self.min_live_cells = float('inf')
        self.change_rate = []
        self.entropy_values = []
        self.grid_history = {}

    def tag_iteration(self, grid):
        self.iterations += 1
        live_cells = np.sum(grid == 255)
        total_cells = grid.size

        # Live cell tracking
        self.live_cell_counts.append(live_cells)
        self.live_cell_percentages.append((live_cells / total_cells) * 100)
        self.max_live_cells = max(self.max_live_cells, live_cells)
        self.min_live_cells = min(self.min_live_cells, live_cells)

        # Calculate entropy
        p = live_cells / total_cells
        entropy = -(p*np.log2(p) + (1-p)*np.log2(1-p)) if p not in [0, 1] else 0
        self.entropy_values.append(entropy)

        # Birth and survival rate calculation
        if self.previous_grid is not None:
            changes = np.sum(self.previous_grid != grid)
            self.change_rate.append((changes / total_cells) * 100)

            births = np.sum((self.previous_grid == 0) & (grid == 255))
            survivals = np.sum((self.previous_grid == 255) & (grid == 255))
            total_previous_live = np.sum(self.previous_grid == 255)

            self.birth_rate.append((births / total_cells) * 100)
            self.survival_rate.append((survivals / total_previous_live) * 100 if total_previous_live > 0 else 0)

            # Check for stabilization and oscillation
            grid_tuple = tuple(grid.flat)
            if grid_tuple in self.grid_history:
                self.stabilized = True
                self.stabilization_time = self.grid_history[grid_tuple]
            else:
                self.grid_history[grid_tuple] = self.iterations

        self.previous_grid = grid.copy()

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
        print(f"Max live cells: {self.max_live_cells}")
        print(f"Min live cells: {self.min_live_cells}")
        print(f"Average change rate: {np.mean(self.change_rate):.2f}%")
        print(f"Average entropy: {np.mean(self.entropy_values):.2f}")
        if self.birth_rate:
            print(f"Average birth rate: {np.mean(self.birth_rate):.2f}%")
        if self.survival_rate:
            print(f"Average survival rate: {np.mean(self.survival_rate):.2f}%")
        if self.stabilized:
            print(f"Stabilization occurred at iteration: {self.stabilization_time}")
        else:
            print("Simulation did not stabilize or entered an oscillation.")

    def get_metrics_dict(self):
        metrics = {
            'iterations': self.iterations,
            'execution_time': time.time() - self.start_time,
            'live_cell_counts': self.live_cell_counts,
            'live_cell_percentages': self.live_cell_percentages,
            'birth_rate': self.birth_rate,
            'survival_rate': self.survival_rate,
            'stabilization_time': self.stabilization_time,
            'max_live_cells': self.max_live_cells,
            'min_live_cells': self.min_live_cells,
            'change_rate': self.change_rate,
            'entropy': self.entropy_values
        }
        return metrics
