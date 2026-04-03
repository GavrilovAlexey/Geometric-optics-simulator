import pygame
from numpy import array
from graphical_functions import units_to_pixels, pixels_to_units, coordinate_units_to_pixels, coordinate_pixels_to_units


class Slider:
    def __init__(self, center, size, value, min_value, max_value, text, accuracy):
        self.point0 = center - size / 2
        self.point1 = center - size * array([1, -1]) / 2
        self.point2 = center + size / 2
        self.point3 = center + size * array([1, -1]) / 2
        self.size = size

        self.activated = False

        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        self.point = self.point0 + self.size * array(
            [(self.value - self.min_value) / (self.max_value - self.min_value), 0.5])

        self.text = text
        self.accuracy = accuracy

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = coordinate_pixels_to_units(array(event.pos))
            self.activated = sum((pos - self.point) ** 2) <= self.size[1] / 2
        elif event.type == pygame.MOUSEMOTION and self.activated:
            rel = pixels_to_units(array(event.rel))
            self.update_value(rel)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.activated = False

    def update_value(self, rel):
        self.value += rel[0] * (self.max_value - self.min_value) / self.size[0]
        if self.value > self.max_value:
            self.value = self.max_value
        elif self.value < self.min_value:
            self.value = self.min_value
        self.point = self.point0 + self.size * array(
            [(self.value - self.min_value) / (self.max_value - self.min_value), 0.5])

    def draw(self):
        from main import screen, activated_color, deactivated_color

        color = activated_color if self.activated else deactivated_color

        font = pygame.font.SysFont("Arial", int(units_to_pixels(1)))
        printed_value = round(self.value, self.accuracy) if self.accuracy > 0 else int(round(self.value, self.accuracy))
        screen.blit(font.render(self.text + f" = {printed_value}", True, color),
                    coordinate_units_to_pixels(array([self.point1[0], -5.5])))

        pygame.draw.aaline(screen, color, coordinate_units_to_pixels(self.point1),
                         coordinate_units_to_pixels(self.point2))
        pygame.draw.aaline(screen, color, coordinate_units_to_pixels(self.point0),
                         coordinate_units_to_pixels(self.point3))

        pygame.draw.circle(screen, color, coordinate_units_to_pixels(self.point0 + self.size * array([0, 0.5])),
                           units_to_pixels(self.size[1] / 2), 1, draw_top_left=True, draw_bottom_left=True)
        pygame.draw.circle(screen, color, coordinate_units_to_pixels(self.point3 + self.size * array([0, 0.5])),
                           units_to_pixels(self.size[1] / 2), 1, draw_top_right=True, draw_bottom_right=True)

        pygame.draw.circle(screen, color, coordinate_units_to_pixels(self.point), units_to_pixels(self.size[1] / 2), 1)
