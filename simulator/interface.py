import pygame
from numpy import array
from simulator.object_classes.base_object import BaseObject
from simulator.object_classes.ray import Ray
from simulator.object_classes.light import Light
from simulator.object_classes.mirror import Mirror
from simulator.object_classes.thin_lens import ThinLens
from simulator.object_classes.medium.medium import Medium
from simulator.object_classes.medium.add_point import AddPoint
from simulator.object_classes.medium.remove_point import RemovePoint
from graphical_functions import coordinate_units_to_pixels, coordinate_pixels_to_units
from widgets.button import Button
from widgets.check_button import CheckButton
from widgets.check_panel import CheckPanel
from widgets.slider import Slider
from icons import exit_icon, grid_icon, delete_icon, ray_icon, light_icon, mirror_icon, thin_lens_icon, prism_icon

positions = []
selection_distance = 1
active_object = BaseObject()

exit_button = Button(array([15, -8]), array([1.5, 1.5]), exit_icon.draw_exit_icon)
grid_button = CheckButton(array([15, -6]), array([1.5, 1.5]), grid_icon.draw_grid_icon)
delete_button = Button(array([-11, -8]), array([1.5, 1.5]), delete_icon.draw_delete_icon)
creation_panel = CheckPanel({
    Ray: CheckButton(array([-15, -6]), array([1.5, 1.5]), ray_icon.draw_ray_icon),
    Light: CheckButton(array([-15, -8]), array([1.5, 1.5]), light_icon.draw_light_icon),
    Mirror: CheckButton(array([-13, -6]), array([1.5, 1.5]), mirror_icon.draw_mirror_icon),
    ThinLens: CheckButton(array([-13, -8]), array([1.5, 1.5]), thin_lens_icon.draw_thin_lens_icon),
    Medium: CheckButton(array([-11, -6]), array([1.5, 1.5]), prism_icon.draw_prism_icon)
})
base_refractive_index_slider = Slider(array([-4, -8]), array([10, 1.5]), 1, 1, 3, "Refractive index", 2)


def update():
    from simulator.engine import objects, lower_bound
    global positions, selection_distance, active_object, exit_button, grid_button, creation_panel, base_refractive_index_slider

    widgets = active_object.get_widgets() + [exit_button, grid_button, delete_button, creation_panel]
    if type(active_object) == BaseObject:
        widgets.append(base_refractive_index_slider)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or exit_button.activated:
            return "exit"
        elif type(active_object) != BaseObject and delete_button.activated:
            if type(active_object) == Medium:
                creation_panel.check_buttons.pop(AddPoint)
                creation_panel.check_buttons.pop(RemovePoint)
            objects.remove(active_object)
            active_object = BaseObject()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = coordinate_pixels_to_units(array(event.pos))
            if position[1] > lower_bound:
                positions.append(position)
                if creation_panel.selected_object == BaseObject:
                    distances_and_objects = []
                    for obj in objects:
                        distance = obj.check(position)
                        if distance > 0:
                            distances_and_objects.append((distance, obj))
                    if distances_and_objects:
                        distance, obj = min(distances_and_objects, key=lambda pair: pair[0])
                        if distance < selection_distance:
                            active_object = obj
                        else:
                            active_object = BaseObject()

                elif len(positions) == creation_panel.selected_object.required_number_of_points:
                    objects.append(creation_panel.selected_object.create(positions))
                    positions.clear()
        for widget in widgets:
            widget.update(event)
        if creation_panel.selected_object not in (BaseObject, AddPoint, RemovePoint):
            active_object = BaseObject()
    return "ok"


def draw_interface():
    from main import screen, background_color
    from simulator.engine import lower_bound
    global exit_button, grid_button, delete_button, creation_panel, base_refractive_index_slider

    pygame.draw.aaline(screen, background_color, coordinate_units_to_pixels(array([-16, lower_bound])),
                       coordinate_units_to_pixels(array([16, lower_bound])))

    if grid_button.activated:
        for y in range(lower_bound + 1, 9):
            pygame.draw.aaline(screen, background_color, coordinate_units_to_pixels(array([-16, y])),
                               coordinate_units_to_pixels(array([16, y])))
        for x in range(-15, 16):
            pygame.draw.aaline(screen, background_color, coordinate_units_to_pixels(array([x, lower_bound])),
                               coordinate_units_to_pixels(array([x, 9])))

    widgets = active_object.get_widgets() + [exit_button, grid_button, delete_button, creation_panel]
    if type(active_object) == BaseObject:
        widgets.append(base_refractive_index_slider)

    for widget in widgets:
        widget.draw()
