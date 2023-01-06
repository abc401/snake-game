import pygame
from fruit import Fruit


class Directions:
    right = pygame.Vector2(1, 0)
    left = pygame.Vector2(-1, 0)
    down = pygame.Vector2(0, 1)
    up = pygame.Vector2(0, -1)


class Snake:
    initial_direction = Directions.right
    initial_length = 1

    def __init__(self, grid_dimensions: tuple[int, int], color: tuple[int, int, int] = (0, 255, 0)):
        self.surface = pygame.display.get_surface()
        self.velocity = self.initial_direction
        self.grid_dimensions = grid_dimensions
        self.color = color

        self.cell_dim = (
            self.surface.get_width()/self.grid_dimensions[0],
            self.surface.get_height()/self.grid_dimensions[1]
        )

        head_pos = pygame.Vector2(self.grid_dimensions[0]/2, self.grid_dimensions[1]/2)
        self.updated = False        # Has the update function been executed

        self.nodes: list[pygame.Vector2] = []
        for i in range(Snake.initial_length):
            self.nodes.append(head_pos + (i * self.velocity))

    def up(self):
        if self.velocity != Directions.down and self.updated:
            self.velocity = Directions.up
            self.updated = False

    def right(self):
        if self.velocity != Directions.left and self.updated:
            self.velocity = Directions.right
            self.updated = False

    def left(self):
        if self.velocity != Directions.right and self.updated:
            self.velocity = Directions.left
            self.updated = False

    def down(self):
        if self.velocity != Directions.up and self.updated:
            self.velocity = Directions.down
            self.updated = False

    def is_out_of_bounds(self):
        return not (
            0 < self.nodes[-1].x < self.grid_dimensions[0]
            and 0 < self.nodes[-1].y < self.grid_dimensions[1]
        )

    def overlap_with_self(self):
        return self.nodes[-1] in self.nodes[:-2]

    def update(self):
        # Add a node in front of the head node in the direction of the velocity
        self.nodes.append(self.nodes[-1] + self.velocity)

        # Delete the tail node
        del self.nodes[0]

        # The update function has been executed
        self.updated = True

    def eaten(self, fruit: Fruit):
        return self.nodes[-1] == fruit.position

    def grow(self):
        self.nodes.append(self.nodes[-1] + self.velocity)

    def draw(self):
        for node in self.nodes:
            pygame.draw.rect(
                self.surface, self.color,
                (
                    int(node.x * self.cell_dim[0]),
                    int(node.y * self.cell_dim[1]),
                    int(self.cell_dim[0]),
                    int(self.cell_dim[1])
                )
            )

