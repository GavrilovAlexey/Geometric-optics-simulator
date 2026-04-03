import pygame
from numpy import array
from graphical_functions import coordinate_pixels_to_units
from widgets.button import Button


class CheckButton(Button):
    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = coordinate_pixels_to_units(array(event.pos))
            self.activated ^= (self.point0 <= pos).all() and (pos <= self.point2).all()