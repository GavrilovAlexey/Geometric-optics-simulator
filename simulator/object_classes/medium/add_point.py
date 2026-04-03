from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.medium.boundary import Boundary

class AddPoint(BaseObject):
    required_number_of_points = 2

    @staticmethod
    def create(positions):
        from simulator.interface import active_object

        boundary = min(active_object.boundaries, key=lambda b: b.check(positions[0]))
        active_object.boundaries.remove(boundary)
        active_object.boundaries.append(Boundary(boundary.a, positions[1]))
        active_object.boundaries.append(Boundary(positions[1], boundary.b))

        return AddPoint()

    def update(self):
        from simulator.engine import objects
        objects.remove(self)