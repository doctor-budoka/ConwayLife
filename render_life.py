import pygame, sys
from pygame.locals import *
import numpy as np

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (63, 63, 63)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def render_matrix(matrix):
    # Set up pygame
    pygame.init()

    dimensions = matrix.shape
    # Set up the window.
    windowSurface = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption("Conway's Game of Life")

    return None
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Draw a green polygon onto the surface.
    pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106),
                                               (236, 277), (56, 277), (0, 106)))

    # Draw some blue lines onto the surface.
    pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
    pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

    # Draw a blue circle onto the surface.
    pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

    # Draw a red ellipse onto the surface.
    pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

    # Draw the text's background rectangle onto the surface.
    pygame.draw.rect(windowSurface, RED, (textRect.left - 20,
                     textRect.top - 20, textRect.width + 40, textRect.height + 40))

    # Get a pixel array of the surface.
    pixArray = pygame.PixelArray(windowSurface)
    pixArray[480][380] = BLACK
    del pixArray

    # Draw the text onto the surface.
    windowSurface.blit(text, textRect)
    # Draw the window onto the screen.
    pygame.display.update()

    # Run the game loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    vector = [0]*9
    vector[4] = 1

    render_matrix(np.reshape(vector, (3, 3)))