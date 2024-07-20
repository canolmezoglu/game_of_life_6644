# grid_manager.py
import numpy as np
import pattern_generator

class GridManager:
    def __init__(self, grid_size=200, divisions=5):
        self.grid_size = grid_size
        self.divisions = divisions
        self.location_size = grid_size // divisions
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.locations = self._create_locations()

    def _create_locations(self):
        locations = {}
        for y in range(self.divisions):
            for x in range(self.divisions):
                name = f"y{y+1}x{x+1}"
                locations[name] = (y * self.location_size, x * self.location_size)
        return locations

    def add_pattern(self, pattern_type, location, offset=(0, 0)):
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")

        start_row, start_col = self.locations[location]
        start_row += offset[0]
        start_col += offset[1]

        pattern = self._generate_pattern(pattern_type, self.location_size)

        end_row = min(start_row + pattern.shape[0], self.grid_size)
        end_col = min(start_col + pattern.shape[1], self.grid_size)

        pattern_height = end_row - start_row
        pattern_width = end_col - start_col

        self.grid[start_row:end_row, start_col:end_col] = np.maximum(
            self.grid[start_row:end_row, start_col:end_col],
            pattern[:pattern_height, :pattern_width]
        )

    def _generate_pattern(self, pattern_type, size):
        if pattern_type == 'random':
            return pattern_generator.random_grid(size)
        elif pattern_type == 'figure_eight':
            return pattern_generator.figure_eight(size)
        elif pattern_type == 'block':
            return pattern_generator.block(size)
        elif pattern_type == 'blinker':
            return pattern_generator.blinker(size)
        elif pattern_type == 'glider':
            return pattern_generator.glider(size)
        elif pattern_type == 'pulsar':
            return pattern_generator.pulsar(size)
        elif pattern_type == 'gosper_glider_gun':
            return pattern_generator.gosper_glider_gun(size)
        else:
            raise ValueError(f"Invalid pattern type: {pattern_type}")

    def get_grid(self):
        return self.grid

    def get_locations(self):
        return list(self.locations.keys())