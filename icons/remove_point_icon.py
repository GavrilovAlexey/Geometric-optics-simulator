from numpy import array
import pygame
from graphical_functions import coordinate_units_to_pixels, units_to_pixels


def draw_remove_point_icon(position, size, activated):
    from main import screen, activated_color, deactivated_color, background_color
    from simulator.interface import active_object
    from simulator.object_classes.medium.medium import Medium

    color = activated_color if activated else deactivated_color
    if type(active_object) == Medium and len(active_object.boundaries) == 3:
        color = background_color

    pygame.draw.rect(screen, color, (coordinate_units_to_pixels(position), units_to_pixels(size)), 1)
    pygame.draw.aaline(screen, color, coordinate_units_to_pixels(position + size * array([0.25, -0.5])),
                     coordinate_units_to_pixels(position + size * array([0.75, -0.5])))