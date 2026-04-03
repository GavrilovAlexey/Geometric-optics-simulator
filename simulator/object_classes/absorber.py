from numpy import array
from numpy.linalg import det, norm
from simulator.engine_functions import distance_to_intersection, intersection_point
from simulator.object_classes.base_object import BaseObject


class Absorber(BaseObject):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.center = (a + b) / 2
        self.size = norm(b - a)
        self.direction = (b - a) / self.size

    def distance(self, ray):
        from simulator.engine import error

        if not det(array([self.direction, ray.direction])):
            return 0

        intersection = intersection_point(ray.start, ray.direction, self.center, self.direction)
        if abs(norm(intersection - self.a) + norm(intersection - self.b) - self.size) >= error:
            return 0
        return distance_to_intersection(ray.start, ray.direction, self.center, self.direction)

    def draw(self):
        pass
