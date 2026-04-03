def distance_to_intersection(point0, direction0, point1, direction1):
    from numpy import array
    from numpy.linalg import det
    return det(array([direction1, point1 - point0])) / det(array([direction1, direction0]))


def intersection_point(point0, direction0, point1, direction1):
    return point0 + direction0 * distance_to_intersection(point0, direction0, point1, direction1)


def refractive_index(point):
    from simulator.engine import base_refractive_index, objects
    from simulator.object_classes.medium.medium import Medium

    layers_and_refractive_indexes = []
    for obj in objects:
        if isinstance(obj, Medium) and obj.is_inside(point):
            layers_and_refractive_indexes.append((obj.layer, obj.refractive_index))

    if layers_and_refractive_indexes:
        return min(layers_and_refractive_indexes, key=lambda pair: pair[0])[1]
    return base_refractive_index
