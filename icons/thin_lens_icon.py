from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_thin_lens_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.5, -0.15])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.85])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.4, -0.65])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.85])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.6, -0.65])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.85])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.4, -0.35])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.15])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.6, -0.35])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.15])))
