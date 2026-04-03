from numpy.linalg import norm
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.medium.boundary import Boundary


class RemovePoint(BaseObject):
    required_number_of_points = 1

    @staticmethod
    def create(positions):
        from simulator.interface import active_object

        points = []
        for boundary in active_object.boundaries:
            points.append(boundary.a)
        point = min(points, key=lambda p: norm(p - positions[0]))

        for boundary in active_object.boundaries:
            if (point == boundary.b).all():
                boundary1 = boundary
            elif (point == boundary.a).all():
                boundary2 = boundary

        active_object.boundaries.remove(boundary1)
        active_object.boundaries.remove(boundary2)
        active_object.boundaries.append(Boundary(boundary1.a, boundary2.b))

        return RemovePoint()

    def update(self):
        from simulator.engine import objects
        objects.remove(self)
