import random
import pygame


class Fruit:
    def __init__(self, grid_dimensions: tuple[int, int], color: tuple[int, int, int] = (255, 0, 0)):
        self.surface = pygame.display.get_surface()
        self.grid_dimensions = grid_dimensions
        self.color = color
        self.cell_dim = (
            self.surface.get_width() / self.grid_dimensions[0],
            self.surface.get_height() / self.grid_dimensions[1]
        )
        self.position = pygame.Vector2(
            random.randint(0, grid_dimensions[0]-2),    # Don't appear on the columns or rows
            random.randint(0, grid_dimensions[1]-2)     # at the extreme side of the window
        )

    def draw(self):
        pygame.draw.rect(
            self.surface, self.color,
            (
                int(self.position.x * self.cell_dim[0]),
                int(self.position.y * self.cell_dim[1]),
                int(self.cell_dim[0]),
                int(self.cell_dim[1])
            )
        )
