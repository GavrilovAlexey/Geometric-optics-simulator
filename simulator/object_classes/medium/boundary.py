import pygame
from numpy import array, sign, cross
from numpy.linalg import det, norm
from simulator.engine_functions import distance_to_intersection, intersection_point
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.ray import Ray
from graphical_functions import coordinate_units_to_pixels
from widgets.point import Point


class Boundary(BaseObject):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.center = (self.a + self.b) / 2
        self.size = norm(self.b - self.a)

        self.direction = (self.b - self.a) / self.size
        self.orthogonal_direction = array([self.direction[1], -self.direction[0]])

        self.points = [Point(self.a.copy()), Point(self.b.copy())]

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

    def distance(self, ray):
        from simulator.engine import error

        if not det(array([self.direction, ray.direction])):
            return 0

        intersection = intersection_point(ray.start, ray.direction, self.center, self.direction)
        if abs(norm(intersection - self.a) + norm(intersection - self.b) - self.size) >= error:
            return 0
        return distance_to_intersection(ray.start, ray.direction, self.center, self.direction)

    def new_ray(self, ray):
        from simulator.engine import error
        from simulator.engine_functions import refractive_index

        orthogonal_direction = self.orthogonal_direction * sign(ray.direction @ self.orthogonal_direction)

        intersection = intersection_point(ray.start, ray.direction, self.center, self.direction)

        n1 = refractive_index(intersection - ray.direction * 100 * error)
        n2 = refractive_index(intersection + ray.direction * 100 * error)
        sin_a1 = cross(orthogonal_direction, ray.direction)
        sin_a2 = n1 / n2 * sin_a1

        if abs(sin_a2) <= 1:
            cos_a2 = (1 - sin_a2 ** 2) ** 0.5
            return Ray(intersection, array([[cos_a2, -sin_a2], [sin_a2, cos_a2]]) @ orthogonal_direction)
        return BaseObject()

    def get_widgets(self):
        return self.points

    def draw(self):
        from main import screen, activated_color
        pygame.draw.aaline(screen, activated_color, coordinate_units_to_pixels(self.a), coordinate_units_to_pixels(self.b))
