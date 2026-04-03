import pygame
from numpy import array
from graphical_functions import units_to_pixels, coordinate_units_to_pixels, coordinate_pixels_to_units


class Button:
    def __init__(self, center, size, icon):
        self.point0 = center - size / 2
        self.point1 = center - size * array([1, -1]) / 2
        self.point2 = center + size / 2
        self.size = size
        self.activated = False

        self.icon = icon

    def update(self, event):
        self.activated = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = coordinate_pixels_to_units(array(event.pos))
            self.activated = (self.point0 <= pos).all() and (pos <= self.point2).all()

    def draw(self):
        from main import screen, activated_color, deactivated_color

        pygame.draw.rect(screen, activated_color if self.activated else deactivated_color,
                         (coordinate_units_to_pixels(self.point1), units_to_pixels(self.size)), 1)
        self.icon(self.point1, self.size, self.activated)
