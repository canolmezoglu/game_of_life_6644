# test_combined_patterns.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grid_manager import GridManager
from game_engine import update_grid


def create_combined_grid():
    grid_manager = GridManager(grid_size=250, divisions=5)  # This creates 50x50 sections
    section_size = grid_manager.location_size

    # Print available locations
    print("Available locations:", grid_manager.get_locations())

    # Define patterns and their offsets
    patterns = [
        ('blinker', [(i, j) for i in range(0, section_size, 5) for j in range(0, section_size, 5)]),
        # ('block', [(i, j) for i in range(0, section_size, 5) for j in range(0, section_size, 5)]),
        ('glider', [(i, j) for i in range(0, section_size, 10) for j in range(0, section_size, 10)]),
        ('pulsar', [(i, j) for i in range(0, section_size, 20) for j in range(0, section_size, 20)]),
        ('figure_eight', [(i, j) for i in range(0, section_size, 12) for j in range(0, section_size, 12)]),
        ('gosper_glider_gun', [(0, 0)]),  # Only one instance of Gosper glider gun
        ('random', [(0, 0)])  # Random pattern will be handled differently
    ]

    for y in range(1, 6):
        for x in range(1, 6):
            location = f'y{y}x{x}'
            pattern_name, offsets = patterns[(y - 1 + x - 1) % len(patterns)]

            if pattern_name == 'random':
                # For random pattern, fill the entire section
                grid_manager.grid[(y - 1) * section_size:y * section_size,
                (x - 1) * section_size:x * section_size] = np.random.choice([0, 255], size=(section_size, section_size),
                                                                            p=[0.5, 0.5])
            else:
                for offset in offsets:
                    grid_manager.add_pattern(pattern_name, location, offset)

    return grid_manager.get_grid()


def animate_grid(grid, frames=1000, interval=50):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title("Combined Patterns - Game of Life (Multiple Instances)")
    img = ax.imshow(grid, interpolation='nearest', cmap='binary')
    plt.axis('off')

    def update(frame):
        img.set_array(update_grid(img.get_array()))
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
    return ani


def main():
    initial_grid = create_combined_grid()
    ani = animate_grid(initial_grid)

    # Save the animation
    ani.save("combined_patterns_multiple_instances_animation.gif", writer='pillow', fps=10)
    print("Animation saved as 'combined_patterns_multiple_instances_animation.gif'")

    # Uncomment the line below if you want to display the animation in a window
    # plt.show()


if __name__ == "__main__":
    main()