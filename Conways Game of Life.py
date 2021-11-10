# By Oscar MacKenzie (https://github.com/omackenzie)

import numpy as np

input_array = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype='bool')


class GameOfLife:
    """The main game class.
    Takes in the starting game grid as a 2D NumPy of booleans.
    """

    def __init__(self, grid):
        self.grid = grid

    def display(self):
        """Displays the grid in an easy to read format,
        mainly for debugging purposes.
        """
        for y, x in np.ndindex(self.grid.shape):
            # Print a new line
            if x == 0:
                print()
            print('  ' if self.grid[y, x] == 1 else '██', end='')

    def n_surrounding_cells(self, y, x):
        """Calculates the number of neighbours of a given cell.
        """

        # Clip the bounds so that all cells are in range
        bounds = np.clip([y - 1, y + 2, x - 1, x + 2], a_min=0, a_max=10)

        total = np.sum(self.grid[bounds[0]:bounds[1], bounds[2]:bounds[3]])
        # A cell can't be its own neighbour, so remove it
        return total - 1 if self.grid[y, x] == 1 else total

    def step(self):
        """Calculates the next generation of the simulation.
        This will update the grid attribute and then return the next generation.
        """
        next_generation = np.zeros(self.grid.shape, dtype='bool')

        for y, x in np.ndindex(self.grid.shape):
            # Any live cell with two or three live neighbours survives
            if self.grid[y, x] == 1 and self.n_surrounding_cells(y, x) in [2, 3]:
                next_generation[y, x] = 1
            # Any dead cell with three live neighbours becomes a live cell
            elif self.grid[y, x] == 0 and self.n_surrounding_cells(y, x) == 3:
                next_generation[y, x] = 1
            # Any other cells are dead
            else:
                next_generation[y, x] = 0

        self.grid = next_generation
        return next_generation


def test():
    # Simulate 10 generations, just for testing
    for _ in range(10):
        game.display()
        print()
        game.step()


if __name__ == '__main__':
    game = GameOfLife(input_array)
    test()