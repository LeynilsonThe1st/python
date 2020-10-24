import pygame, random
from pygame.locals import *
import time


def on_grid_random():
    x = random.randint(0,580)
    y = random.randint(0,580)
    return (x//20 * 20, y//20 * 20)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
# snake_skin = pygame.Surface((10,10))
snake_skin = pygame.image.load("/Users/leynilson_harden/Dropbox/Programação/PycharmProjects/python/sprite.png").convert()
# snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
# apple = pygame.Surface((20,20))
apple = pygame.image.load("/Users/leynilson_harden/Dropbox/Programação/PycharmProjects/python/squares.jpg").convert()

# apple.fill((255,0,0))
# snake_skin.fill((
#         random.randint(100,255),
#         random.randint(100,255),
#         random.randint(100,255)
#         ))

my_direction = LEFT

clock = pygame.time.Clock()


while True:
    # clock.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and not my_direction == DOWN:
                my_direction = UP
            if event.key == K_DOWN and not my_direction == UP:
                my_direction = DOWN
            if event.key == K_LEFT and not my_direction == RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and not my_direction == LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        # snake_skin.fill((
        # random.randint(0,255),
        # random.randint(0,255),
        # random.randint(0,255)
        # ))
        apple_pos = on_grid_random()
        snake.append((0,0))

    if snake[0] in snake[1:]:
        time.sleep(5)
        pygame.quit()

    if snake[0][0] > 600 or snake[0][1] > 600 or snake[0][0] <= -1 or snake[0][1] <= -1:
        time.sleep(5)
        pygame.quit()

    for i in range(len(snake) - 1, 0, - 1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    screen.fill((255, 255, 255))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    time.sleep (90.0 / 1000.0)
    pygame.display.update()
