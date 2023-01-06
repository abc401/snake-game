import pygame
from snake import Snake
from fruit import Fruit


dimensions = (600, 600)
bgc = (255, 255, 255)
grid_dimensions = (50, 50)

pygame.init()
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

f = Fruit(grid_dimensions)
s = Snake(grid_dimensions)
game_over = False


def draw():
    screen.fill((255, 255, 255))
    s.draw()
    f.draw()
    # pygame.draw.circle(screen, (0, 0, 0), (dimensions[0]/2, dimensions[1]/2), 10)

    pygame.display.update()


def update():
    global game_over
    game_over = s.is_out_of_bounds() or s.overlap_with_self()

    if not game_over:
        s.update()

        global f
        if s.eaten(f):
            s.grow()
            f = Fruit(grid_dimensions)


def main():
    running = True
    while running:
        update()
        draw()
        clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    s.up()

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    s.down()

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    s.left()

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    s.right()

    pygame.quit()


if __name__ == '__main__':
    main()
