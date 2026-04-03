from numpy import array
from numpy.linalg import norm
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.medium.boundary import Boundary
from simulator.object_classes.ray import Ray
from widgets.slider import Slider


class Medium(BaseObject):
    def __init__(self, refractive_index, points, layer):
        self.refractive_index = refractive_index
        self.refractive_index_slider = Slider(array([-2.5, -8]), array([9, 1.5]), self.refractive_index, 1, 3, "n", 2)

        self.boundaries = []
        for i in range(len(points)):
            self.boundaries.append(Boundary(points[i - 1], points[i]))

        self.layer = layer
        self.layer_slider = Slider(array([8.5, -8]), array([9, 1.5]), self.layer, 0, 10, "Layer", 0)

        self.activated = False

    def is_inside(self, point):
        from simulator.engine import error

        ray = Ray(point, array([1., 0.]))
        number_of_intersections = 0
        for boundary in self.boundaries:
            distance = boundary.distance(ray)
            if distance > error:
                number_of_intersections += 1
            if (boundary.a - point) @ array([1., 0.]) == norm(boundary.a - point):
                number_of_intersections -= 1
        return bool(number_of_intersections % 2)

    required_number_of_points = 3

    @staticmethod
    def create(positions):
        from simulator.engine import base_refractive_index
        return Medium(base_refractive_index, positions, 0)

    def check(self, position):
        distances = []
        for boundary in self.boundaries:
            distance = boundary.check(position)
            if distance > 0:
                distances.append(distance)
        if distances:
            return min(distances)
        return 0

    def update(self):
        from simulator.object_classes.medium import add_point, remove_point
        from simulator.interface import active_object, creation_panel
        from widgets.check_button import CheckButton
        from icons import add_point_icon, remove_point_icon

        if self == active_object and not self.activated:
            creation_panel.check_buttons[add_point.AddPoint] =\
                CheckButton(array([-9, -6]), array([1.5, 1.5]), add_point_icon.draw_add_point_icon)
            creation_panel.check_buttons[remove_point.RemovePoint] =\
                CheckButton(array([-9, -8]), array([1.5, 1.5]), remove_point_icon.draw_remove_point_icon)
            self.activated = True
        elif self != active_object and self.activated:
            if type(active_object) != Medium:
                creation_panel.check_buttons.pop(add_point.AddPoint)
                creation_panel.check_buttons.pop(remove_point.RemovePoint)
            self.activated = False

        self.refractive_index = self.refractive_index_slider.value
        self.layer = round(self.layer_slider.value)

        for boundary in self.boundaries:
            boundary.update()

    def distance(self, ray):
        return ray.find_min_distance_to_object(self.boundaries)[0]

    def new_ray(self, ray):
        boundary = ray.find_min_distance_to_object(self.boundaries)[1]
        return boundary.new_ray(ray)

    def get_widgets(self):
        widgets = []
        for boundary in self.boundaries:
            widgets.extend(boundary.get_widgets())
        return widgets + [self.refractive_index_slider, self.layer_slider]

    def draw(self):
        for boundary in self.boundaries:
            boundary.draw()
