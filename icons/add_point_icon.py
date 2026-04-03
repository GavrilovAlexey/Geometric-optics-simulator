from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_add_point_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.25, -0.5])),
                       coordinate_units_to_pixels(position + size * array([0.75, -0.5])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.5, -0.25])),
                       coordinate_units_to_pixels(position + size * array([0.5, -0.75])))
