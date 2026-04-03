from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_mirror_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.675, -0.15])),
                     coordinate_units_to_pixels(position + size * array([0.675, -0.85])))

    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.325, -0.85])),
                     coordinate_units_to_pixels(position + size * array([0.675, -0.5])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.45, -0.375])),
                     coordinate_units_to_pixels(position + size * array([0.55, -0.375])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.55, -0.275])),
                     coordinate_units_to_pixels(position + size * array([0.55, -0.375])))

    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.325, -0.15])),
                     coordinate_units_to_pixels(position + size * array([0.675, -0.5])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.55, -0.725])),
                     coordinate_units_to_pixels(position + size * array([0.45, -0.725])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.45, -0.625])),
                     coordinate_units_to_pixels(position + size * array([0.45, -0.725])))
