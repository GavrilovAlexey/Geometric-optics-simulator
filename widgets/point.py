import pygame
from numpy import array, maximum, minimum
from graphical_functions import units_to_pixels, pixels_to_units, coordinate_units_to_pixels, coordinate_pixels_to_units


class Point:
    def __init__(self, position):
        self.position = position
        self.r = 0.15

        self.activated = False

    def update(self, event):
        from simulator.engine import error
        from simulator.engine import lower_bound

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = coordinate_pixels_to_units(array(event.pos))
            self.activated = sum((pos - self.position) ** 2) <= (2 * self.r) ** 2
        elif event.type == pygame.MOUSEMOTION and self.activated:
            rel = pixels_to_units(array(event.rel))
            self.position += rel * array([1., -1.])
            self.position = minimum(maximum(self.position, array([-16, lower_bound + error])), array([16, 9]))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.activated = False

    def draw(self):
        from main import screen, activated_color, deactivated_color, background_color

        color = deactivated_color  if self.activated else background_color
        pygame.draw.circle(screen, color, coordinate_units_to_pixels(self.position), units_to_pixels(self.r))
        pygame.draw.circle(screen, activated_color, coordinate_units_to_pixels(self.position),
                           units_to_pixels(self.r) / 2)
