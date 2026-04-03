import pygame
from numpy import array
from numpy.linalg import norm
from simulator.engine_functions import intersection_point
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.ray import Ray
from graphical_functions import coordinate_units_to_pixels
from widgets.point import Point
from widgets.slider import Slider


class Light(BaseObject):
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.center = (self.a + self.b) / 2
        self.size = norm(self.b - self.a)

        self.direction = (self.b - self.a) / self.size
        self.orthogonal_direction = array([self.direction[1], -self.direction[0]])

        self.n = n
        self.rays = [Ray(self.a + (self.b - self.a) * i / (self.n - 1), self.orthogonal_direction) for i in
                     range(self.n)]

        self.points = [Point(self.a.copy()), Point(self.b.copy())]
        self.slider = Slider(array([-4, -8]), array([10, 1.5]), self.n, 3, 100, "Number of rays", 0)

    required_number_of_points = 2

    @staticmethod
    def create(positions):
        return Light(positions[0], positions[1], max(int(norm(positions[1] - positions[0])), 3))

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

        self.n = round(self.slider.value)
        self.rays = [Ray(self.a + (self.b - self.a) * i / (self.n - 1), self.orthogonal_direction) for i in
                     range(self.n)]

    def get_widgets(self):
        return self.points + [self.slider]

    def draw(self):
        from main import screen, activated_color
        from simulator.engine import number_of_iterations

        pygame.draw.aaline(screen, activated_color, coordinate_units_to_pixels(self.a), coordinate_units_to_pixels(self.b))
        for ray in self.rays:
            ray.draw(number_of_iterations)
