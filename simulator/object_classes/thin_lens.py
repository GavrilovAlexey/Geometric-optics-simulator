import pygame
from numpy import array
from numpy.linalg import det, norm
from simulator.engine_functions import distance_to_intersection, intersection_point
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.ray import Ray
from graphical_functions import coordinate_units_to_pixels
from widgets.point import Point
from widgets.slider import Slider


class ThinLens(BaseObject):
    def __init__(self, a, b, refractive_index, r1, r2):
        self.a = a
        self.b = b
        self.center = (self.a + self.b) / 2
        self.size = norm(self.b - self.a)

        self.direction = (self.b - self.a) / self.size
        self.orthogonal_direction = array([self.direction[1], -self.direction[0]])

        self.refractive_index = refractive_index
        self.r1 = r1
        self.r2 = r2

        self.points = [Point(self.a.copy()), Point(self.b.copy())]
        self.sliders = [Slider(array([-6, -8]), array([6, 1.5]), refractive_index, 1, 3, "n", 2),
                        Slider(array([2, -8]), array([6, 1.5]), 1, -1, 1, "r1", 1),
                        Slider(array([10, -8]), array([6, 1.5]), 1, -1, 1, "r2", 1),]

    required_number_of_points = 2

    @staticmethod
    def create(positions):
        from simulator.engine import base_refractive_index
        return ThinLens(positions[0], positions[1], base_refractive_index, 1, 1)

    def check(self, position):
        from simulator.engine import error

        intersection = intersection_point(position, self.orthogonal_direction, self.center, self.direction)
        if abs(norm(intersection - self.a) + norm(intersection - self.b) - self.size) >= error:
            return min(norm(position - self.a), norm(position - self.b))
        return norm(position - intersection)

    def update(self):
        self.a = self.points[0].position.copy()
        self.b = self.points[1].position.copy()
        self.center = (self.a + self.b) / 2
        self.size = norm(self.b - self.a)

        self.direction = (self.b - self.a) / self.size
        self.orthogonal_direction = array([self.direction[1], -self.direction[0]])

        self.refractive_index, self.r1, self.r2 = map(lambda slider: slider.value, self.sliders)

    def distance(self, ray):
        from simulator.engine import error
        from simulator.engine_functions import refractive_index

        if not det(array([self.direction, ray.direction])):
            return 0

        intersection = intersection_point(ray.start, ray.direction, self.center, self.direction)
        optical_power = (self.refractive_index / refractive_index(intersection) - 1) * (1 / self.r1 + 1 / self.r2)

        if not optical_power or abs(norm(intersection - self.a) + norm(intersection - self.b) - self.size) >= error:
            return 0
        return distance_to_intersection(ray.start, ray.direction, self.center, self.direction)

    def new_ray(self, ray):
        from simulator.engine_functions import refractive_index

        intersection = intersection_point(ray.start, ray.direction, self.center, self.direction)
        optical_power = (self.refractive_index / refractive_index(intersection) - 1) * (1 / self.r1 + 1 / self.r2)
        focus1 = self.center + self.orthogonal_direction / optical_power
        focus2 = self.center - self.orthogonal_direction / optical_power

        if norm(ray.start - focus1) * optical_power > norm(ray.start - focus2) * optical_power:
            focus = focus1
        else:
            focus = focus2

        point = intersection_point(self.center, ray.direction, focus, self.direction)
        start_side = det(array([ray.start - self.center, self.direction]))
        point_side = det(array([point - self.center, self.direction]))

        if start_side * point_side < 0:
            return Ray(intersection, (point - intersection))
        else:
            return Ray(intersection, -(point - intersection))

    def get_widgets(self):
        return self.points + self.sliders

    def draw(self):
        from main import screen, activated_color
        from simulator.engine import base_refractive_index

        pygame.draw.aaline(screen, activated_color, coordinate_units_to_pixels(self.a),
                           coordinate_units_to_pixels(self.b))

        optical_power = (self.refractive_index / base_refractive_index - 1) * (1 / self.r1 + 1 / self.r2)
        if optical_power > 0:
            pygame.draw.aalines(screen, activated_color, False, [
                coordinate_units_to_pixels(self.a + 3 * (self.direction - self.orthogonal_direction) * self.size / 50),
                coordinate_units_to_pixels(self.a),
                coordinate_units_to_pixels(self.a + 3 * (self.direction + self.orthogonal_direction) * self.size / 50)
            ])
            pygame.draw.aalines(screen, activated_color, False, [
                coordinate_units_to_pixels(self.b + 3 * (-self.direction - self.orthogonal_direction) * self.size / 50),
                coordinate_units_to_pixels(self.b),
                coordinate_units_to_pixels(self.b + 3 * (-self.direction + self.orthogonal_direction) * self.size / 50)
            ])
        elif optical_power == 0:
            pygame.draw.aaline(screen, activated_color,
                               coordinate_units_to_pixels(self.a - 3 * self.orthogonal_direction * self.size / 50),
                               coordinate_units_to_pixels(self.a + 3 * self.orthogonal_direction * self.size / 50))
            pygame.draw.aaline(screen, activated_color,
                               coordinate_units_to_pixels(self.b - 3 * self.orthogonal_direction * self.size / 50),
                               coordinate_units_to_pixels(self.b + 3 * self.orthogonal_direction * self.size / 50))
        else:
            pygame.draw.aalines(screen, activated_color, False, [
                coordinate_units_to_pixels(self.a + 3 * (-self.direction - self.orthogonal_direction) * self.size / 50),
                coordinate_units_to_pixels(self.a),
                coordinate_units_to_pixels(self.a + 3 * (-self.direction + self.orthogonal_direction) * self.size / 50)
            ])
            pygame.draw.aalines(screen, activated_color, False, [
                coordinate_units_to_pixels(self.b + 3 * (self.direction - self.orthogonal_direction) * self.size / 50),
                coordinate_units_to_pixels(self.b),
                coordinate_units_to_pixels(self.b + 3 * (self.direction + self.orthogonal_direction) * self.size / 50)
            ])
