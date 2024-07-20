# test_patterns.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pattern_generator import (
    random_grid, figure_eight, block, blinker, glider, pulsar, gosper_glider_gun
)
from game_engine import update_grid

def animate_pattern(initial_grid, title, frames=200, interval=50):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title(title)
    img = ax.imshow(initial_grid, interpolation='nearest', cmap='binary')
    plt.axis('off')

    def update(frame):
        img.set_data(update_grid(img.get_array()))
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
    ani.save(f"patterns_{title}.gif", writer='Pillow', fps=10)
    plt.close()
def test_patterns():
    patterns = [
        (random_grid(40), "Random Grid (50x50)"),
        (figure_eight(40), "Figure Eight (50x50)"),
        (block(40), "Block (50x50)"),
        (blinker(40), "Blinker (50x50)"),
        (glider(40), "Glider (50x50)"),
        (pulsar(40), "Pulsar (50x50)"),
        (gosper_glider_gun(40), "Gosper Glider Gun (50x50)")
    ]

    for pattern, title in patterns:
        print(f"Animating: {title}")
        animate_pattern(pattern, title)
        input("Press Enter to continue to the next pattern...")

if __name__ == "__main__":
    test_patterns()