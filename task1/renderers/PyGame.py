import pygame

from classes.data import Data


def start(color: Data):
    pygame.init()
    win = pygame.display.set_mode((200, 420))
    pygame.display.set_caption("Traffic Color")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(10)
        colors = [(22, 0, 0), (22, 122, 0), (0, 22, 0)]
        if color.s == "r":
            colors = [(255, 0, 0), (22, 22, 0), (0, 22, 0)]
        elif color.s == "y":
            colors = [(22, 0, 0), (255, 255, 0), (0, 22, 0)]
        elif color.s == "g":
            colors = [(22, 0, 0), (22, 22, 0), (0, 255, 0)]
        pygame.draw.circle(win, colors[0], (100, 100), 50)
        pygame.draw.circle(win, colors[1], (100, 210), 50)
        pygame.draw.circle(win, colors[2], (100, 320), 50)
        pygame.display.update()