import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Code_Clash")

client_Number = 0


def redraw_window():
    win.fill((255, 255, 255))
    pygame.display.update()
