from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels


def draw_light_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color

    color = activated_color if activated else deactivated_color
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.15, -0.85])),
                     coordinate_units_to_pixels(position + size * array([0.85, -0.15])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.4, -0.4])),
                     coordinate_units_to_pixels(position + size * array([0.6, -0.4])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.6, -0.6])),
                     coordinate_units_to_pixels(position + size * array([0.6, -0.4])))

    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.15, -0.4])),
                     coordinate_units_to_pixels(position + size * array([0.4, -0.15])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.225, -0.225])),
                     coordinate_units_to_pixels(position + size * array([0.325, -0.225])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.325, -0.325])),
                     coordinate_units_to_pixels(position + size * array([0.325, -0.225])))

    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.6, -0.85])),
                     coordinate_units_to_pixels(position + size * array([0.85, -0.6])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.675, -0.675])),
                     coordinate_units_to_pixels(position + size * array([0.775, -0.675])))
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.775, -0.775])),
                     coordinate_units_to_pixels(position + size * array([0.775, -0.675])))
