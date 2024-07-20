# run_experiment.py
import game_engine
from grid_manager import GridManager
from metrics import GameOfLifeMetrics


def run_experiment(grid_size=200, divisions=5, iterations=150, patterns=None):
    if patterns is None:
        patterns = [('figure_eight', 'middle_center')]

    grid_manager = GridManager(grid_size, divisions)

    for pattern_type, location in patterns:
        grid_manager.add_pattern(pattern_type, location)

    grid = grid_manager.get_grid()
    metrics = GameOfLifeMetrics()

    for _ in range(iterations):
        grid = game_engine.update_grid(grid)
        metrics.tag_iteration(grid)

    return grid, metrics


def print_grid(grid):
    for row in grid:
        print(''.join(['■' if cell == 255 else '□' for cell in row]))


if __name__ == '__main__':
    # Example usage
    patterns = [
        ('figure_eight', 'middle_center'),
        ('random', 'top_left'),
        ('figure_eight', 'bottom_right')
    ]
    final_grid, metrics = run_experiment(patterns=patterns)

    print("Final Grid State:")
    print_grid(final_grid)
    print("\nPerformance Metrics:")
    metrics.print_metrics()

    print("\nAvailable Grid Locations:")
    grid_manager = GridManager()
    print(", ".join(grid_manager.get_locations()))