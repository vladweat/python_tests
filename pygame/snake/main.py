import pygame

SPEED = 1.5

FPS = 60
WIN_WIDTH = 600
WIN_HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

r = 30
x = 0
y = WIN_HEIGHT // 2

while 1:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLACK, (x + r, y), r, 5)
    pygame.display.update()

    if x >= WIN_WIDTH - r * 2:
        reach = True
    elif x <= 0:
        reach = False

    if reach:
        x -= 4
    if not reach:
        x += 4

    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
