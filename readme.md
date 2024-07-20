# Game of Life Simulation

This project implements Conway's Game of Life, a cellular automaton simulation. It features a customizable grid, various initial patterns, and metrics tracking for analyzing the simulation's behavior.

## Components

### 1. game_engine.py
The core logic of the Game of Life simulation. It defines the rules for cell evolution and handles the grid updates for each generation.

Key functions:
- `create_grid(N)`: Initializes an empty grid of size N x N.
- `update_grid(grid)`: Applies the Game of Life rules to update the grid for the next generation.

### 2. pattern_generator.py
Generates initial patterns for the simulation.

Key functions:
- `random_grid(N, p_alive=0.2)`: Creates a random initial grid with a specified probability of live cells.
- `figure_eight(N)`: Generates a "figure eight" pattern, scaled to fit the grid size.

### 3. grid_manager.py
Manages the placement of patterns on the grid and handles grid divisions.

Key class:
- `GridManager`: Allows adding patterns to specific locations on the grid.

### 4. visualization.py
Handles the visualization of the Game of Life simulation using matplotlib.

Key functions:
- `create_figure(grid)`: Sets up the initial plot.
- `update_frame(frameNum, img, grid, update_func)`: Updates the plot for each frame of the animation.
- `animate_game(grid, update_func, frames=150, interval=50)`: Creates an animation of the Game of Life simulation.
- `save_animation(ani, filename='game_of_life.gif')`: Saves the animation as a GIF.
- `show_animation()`: Displays the animation.

### 5. metrics_tracker.py
Tracks and analyzes metrics for the Game of Life simulation.

Key class:
- `GameOfLifeMetrics`: Collects data on live cell counts, percentages, and execution time.

### 6. run_experiment.py
The main script to run the Game of Life simulation experiments.

Key function:
- `run_experiment(grid_size=200, divisions=5, iterations=150, patterns=None)`: Sets up and runs a complete simulation with specified parameters.

## Usage

To run a Game of Life simulation:

1. Ensure all dependencies are installed (numpy, matplotlib).
2. Modify the patterns and parameters in `run_experiment.py` as desired.
3. Run `python run_experiment.py`.

Example:

```python
patterns = [
    ('figure_eight', 'middle_center'),
    ('random', 'top_left'),
    ('figure_eight', 'bottom_right')
]
final_grid, metrics = run_experiment(patterns=patterns)
print_grid(final_grid)
metrics.print_metrics()
```

This will run a simulation with a figure-eight pattern in the center, random cells in the top-left, and another figure-eight in the bottom-right. It will then print the final grid state and performance metrics.

## Customization

- Adjust grid size, number of iterations, and initial patterns in `run_experiment.py`.
- Modify or add new patterns in `pattern_generator.py`.
- Customize metrics tracking in `metrics_tracker.py`.

Enjoy exploring the fascinating world of cellular automata with this Game of Life simulation!