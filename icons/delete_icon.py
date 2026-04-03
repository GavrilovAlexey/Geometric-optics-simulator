from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_delete_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aalines(screen, color, False, [
        coordinate_units_to_pixels(position + size * array([0.3, -0.35])),
        coordinate_units_to_pixels(position + size * array([0.3, -0.85])),
        coordinate_units_to_pixels(position + size * array([0.7, -0.85])),
        coordinate_units_to_pixels(position + size * array([0.7, -0.35]))
    ])

    pygame.draw.aalines(screen, color, True, [
        coordinate_units_to_pixels(position + size * array([0.2, -0.25])),
        coordinate_units_to_pixels(position + size * array([0.2, -0.35])),
        coordinate_units_to_pixels(position + size * array([0.8, -0.35])),
        coordinate_units_to_pixels(position + size * array([0.8, -0.25]))
    ])

    pygame.draw.aalines(screen, color, False, [
        coordinate_units_to_pixels(position + size * array([0.6, -0.25])),
        coordinate_units_to_pixels(position + size * array([0.6, -0.15])),
        coordinate_units_to_pixels(position + size * array([0.4, -0.15])),
        coordinate_units_to_pixels(position + size * array([0.4, -0.25]))
    ])

    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.4, -0.45])),
                     coordinate_units_to_pixels(position + size * array([0.4, -0.75])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.5, -0.45])),
                     coordinate_units_to_pixels(position + size * array([0.5, -0.75])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.6, -0.45])),
                     coordinate_units_to_pixels(position + size * array([0.6, -0.75])))
