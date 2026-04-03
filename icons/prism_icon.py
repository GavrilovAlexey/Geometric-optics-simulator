from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_prism_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.15, -0.85])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.15])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.5, -0.15])),
                     coordinate_units_to_pixels(position + size * array([0.85, -0.85])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.85, -0.85])),
                     coordinate_units_to_pixels(position + size * array([0.15, -0.85])))
