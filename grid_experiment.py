import numpy as np
from grid_manager import GridManager
from game_engine import update_grid
from metrics import GameOfLifeMetrics


def create_experiment_grid(config, grid_size=250, divisions=5):
    grid_manager = GridManager(grid_size=grid_size, divisions=divisions)

    # Place specified patterns
    for location, pattern in config.items():
        grid_manager.add_pattern(pattern, location)

    # Fill unspecified locations with random patterns
    all_locations = set(grid_manager.get_locations())
    unspecified_locations = all_locations - set(config.keys())
    for location in unspecified_locations:
        grid_manager.add_pattern('random', location)

    return grid_manager.get_grid()


def run_experiment(config, iterations=10000):
    initial_grid = create_experiment_grid(config)
    metrics = GameOfLifeMetrics()

    grid = initial_grid.copy()
    for _ in range(iterations):
        grid = update_grid(grid)
        metrics.tag_iteration(grid)

    return grid, metrics


# Define the 10 configurations
configurations = [
    # Configuration 1: Asymmetric pattern distribution
    {
        'y1x1': 'blinker', 'y1x5': 'glider', 'y2x2': 'pulsar',
        'y3x4': 'figure_eight', 'y5x3': 'gosper_glider_gun',
        'y4x1': 'block', 'y2x5': 'random'
    },

    # Configuration 2: Density gradient (high to low)
    {
        'y1x1': 'gosper_glider_gun', 'y1x2': 'pulsar', 'y1x3': 'figure_eight',
        'y2x1': 'pulsar', 'y2x2': 'blinker', 'y2x3': 'glider',
        'y3x1': 'figure_eight', 'y3x2': 'glider', 'y3x3': 'block',
        'y4x1': 'glider', 'y4x2': 'block', 'y4x3': 'random',
        'y5x1': 'block', 'y5x2': 'random', 'y5x3': 'random'
    },

    # Configuration 3: Central complex structure surrounded by simpler patterns
    {
        'y3x3': 'gosper_glider_gun',
        'y2x2': 'pulsar', 'y2x4': 'pulsar', 'y4x2': 'pulsar', 'y4x4': 'pulsar',
        'y1x1': 'blinker', 'y1x5': 'blinker', 'y5x1': 'blinker', 'y5x5': 'blinker',
        'y3x1': 'glider', 'y3x5': 'glider', 'y1x3': 'glider', 'y5x3': 'glider'
    },

    # Configuration 4: Asymmetric collision course
    {
        'y1x1': 'gosper_glider_gun', 'y5x5': 'pulsar',
        'y1x5': 'glider', 'y2x4': 'glider', 'y3x3': 'glider',
        'y4x2': 'figure_eight', 'y5x1': 'figure_eight'
    },

    # Configuration 5: Edge-centric pattern with central disturbance
    {
        'y1x1': 'blinker', 'y1x3': 'pulsar', 'y1x5': 'blinker',
        'y3x1': 'pulsar', 'y3x5': 'pulsar',
        'y5x1': 'blinker', 'y5x3': 'pulsar', 'y5x5': 'blinker',
        'y3x3': 'gosper_glider_gun'
    },

    # Configuration 6: Diagonal density gradient
    {
        'y1x1': 'gosper_glider_gun', 'y1x2': 'pulsar', 'y2x1': 'pulsar',
        'y2x2': 'figure_eight', 'y2x3': 'glider', 'y3x2': 'glider',
        'y3x3': 'blinker', 'y3x4': 'block', 'y4x3': 'block',
        'y4x4': 'random', 'y4x5': 'random', 'y5x4': 'random', 'y5x5': 'random'
    },

    # Configuration 7: Concentric pattern rings
    {
        'y3x3': 'gosper_glider_gun',
        'y2x2': 'blinker', 'y2x4': 'blinker', 'y4x2': 'blinker', 'y4x4': 'blinker',
        'y1x1': 'glider', 'y1x5': 'glider', 'y5x1': 'glider', 'y5x5': 'glider',
        'y1x3': 'pulsar', 'y3x1': 'pulsar', 'y3x5': 'pulsar', 'y5x3': 'pulsar'
    },

    # Configuration 8: Asymmetric split (complex left, simple right)
    {
        'y1x1': 'gosper_glider_gun', 'y3x1': 'pulsar', 'y5x1': 'figure_eight',
        'y1x2': 'pulsar', 'y3x2': 'figure_eight', 'y5x2': 'glider',
        'y1x4': 'blinker', 'y3x4': 'block', 'y5x4': 'blinker',
        'y1x5': 'block', 'y3x5': 'blinker', 'y5x5': 'block'
    },

    # Configuration 9: Spiral pattern
    {
        'y1x3': 'gosper_glider_gun', 'y2x4': 'pulsar', 'y3x5': 'figure_eight',
        'y4x4': 'glider', 'y5x3': 'blinker', 'y4x2': 'block',
        'y3x1': 'pulsar', 'y2x2': 'glider'
    },

    # Configuration 10: Checkerboard with alternating complex and simple patterns
    {
        'y1x1': 'gosper_glider_gun', 'y1x3': 'block', 'y1x5': 'pulsar',
        'y3x1': 'block', 'y3x3': 'figure_eight', 'y3x5': 'block',
        'y5x1': 'pulsar', 'y5x3': 'block', 'y5x5': 'gosper_glider_gun'
    }

]
configurations = [
{
    'y1x1': 'gosper_glider_gun', 'y1x2': 'pulsar', 'y1x3': 'figure_eight',
    'y2x1': 'pulsar', 'y2x2': 'blinker', 'y2x3': 'glider',
    'y3x1': 'figure_eight', 'y3x2': 'glider', 'y3x3': 'block',
    'y4x4': 'block', 'y4x5': 'blinker',
    'y5x4': 'blinker', 'y5x5': 'block'
},
{
    'y1x1': 'gosper_glider_gun', 'y1x5': 'gosper_glider_gun',
    'y5x1': 'gosper_glider_gun', 'y5x5': 'gosper_glider_gun',
    'y3x3': 'pulsar'
},
{
    'y1x1': 'gosper_glider_gun', 'y5x5': 'gosper_glider_gun',
    'y1x5': 'block', 'y2x4': 'block', 'y3x3': 'block', 'y4x2': 'block', 'y5x1': 'block',
    'y2x2': 'blinker', 'y3x1': 'blinker', 'y3x5': 'blinker', 'y4x4': 'blinker'
},
{
    'y3x3': 'gosper_glider_gun',
    'y2x2': 'pulsar', 'y2x4': 'pulsar', 'y4x2': 'pulsar', 'y4x4': 'pulsar',
    'y1x1': 'glider', 'y1x5': 'glider', 'y5x1': 'glider', 'y5x5': 'glider'
},
{
    'y1x1': 'gosper_glider_gun', 'y2x3': 'pulsar', 'y3x5': 'figure_eight',
    'y4x2': 'glider', 'y5x4': 'blinker',
    'y1x5': 'block', 'y3x1': 'block', 'y5x3': 'block',
    'y2x5': 'random', 'y4x4': 'random', 'y5x1': 'random'
}
]


def main():
    for i, config in enumerate(configurations, 1):
        print(f"Running experiment for Configuration {i}")
        final_grid, metrics = run_experiment(config)

        # Print metrics
        print(f"Results for Configuration {i}:")
        metrics.print_metrics()
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()