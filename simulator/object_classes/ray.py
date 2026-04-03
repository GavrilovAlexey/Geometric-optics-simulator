import pygame
from numpy import array, radians, cos, sin, angle
from numpy.linalg import norm
from simulator.engine_functions import intersection_point
from simulator.object_classes.base_object import BaseObject
from graphical_functions import coordinate_units_to_pixels
from widgets.point import Point
from widgets.slider import Slider


class Ray(BaseObject):
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction / norm(direction)
        self.orthogonal_direction = array([self.direction[1], -self.direction[0]])

        self.slider = Slider(array([-4, -8]), array([10, 1.5]), angle(complex(*direction), deg=True), -180, 180, "Angle", 0)
        self.point = Point(self.start.copy())

    required_number_of_points = 2
    @staticmethod
    def create(positions):
        return Ray(positions[0], positions[1] - positions[0])

    def check(self, position):
        from simulator.engine import objects, error

        intersection = intersection_point(position, self.orthogonal_direction, self.start, self.direction)
        size = self.find_min_distance_to_object(objects)[0]
        a = self.start
        b = a + self.direction * size

        if abs(norm(intersection - a) + norm(intersection - b) - size) >= error:
            return min(norm(position - a), norm(position - b))
        return norm(position - intersection)

    def update(self):
        self.start = self.point.position.copy()
        self.direction = array([cos(radians(self.slider.value)), sin(radians(self.slider.value))])

    def find_min_distance_to_object(self, objects):
        from simulator.engine import error

        distances_and_objects = []
        for obj in objects:
            distance = obj.distance(self)
            if distance > error:
                distances_and_objects.append((distance, obj))

        if distances_and_objects:
            return min(distances_and_objects, key=lambda pair: pair[0])
        return 0, BaseObject()

    def get_widgets(self):
        return [self.slider, self.point]

    def draw(self, n):
        from main import screen, activated_color
        from simulator.engine import objects

        if not n:
            return

        distance, obj = self.find_min_distance_to_object(objects)
        pygame.draw.aaline(screen, activated_color, coordinate_units_to_pixels(self.start),
                           coordinate_units_to_pixels(self.start + self.direction * distance))

        new_ray = obj.new_ray(self)
        if isinstance(new_ray, Ray):
            new_ray.draw(n - 1)
