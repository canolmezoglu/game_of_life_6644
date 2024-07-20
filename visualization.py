# visualization.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_figure(grid):
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    return fig, img

def update_frame(frameNum, img, grid, update_func):
    new_grid = update_func(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

def animate_game(grid, update_func, frames=150, interval=50):
    fig, img = create_figure(grid)
    ani = animation.FuncAnimation(
        fig, update_frame, fargs=(img, grid, update_func),
        frames=frames, interval=interval, save_count=50, blit=True
    )
    return ani

def save_animation(ani, filename='game_of_life.gif'):
    ani.save(filename, writer='Pillow', fps=10)

def show_animation():
    plt.show()