import pygame
from numpy import array
from simulator.object_classes.base_object import BaseObject
from graphical_functions import coordinate_pixels_to_units


class CheckPanel:
    def __init__(self, check_buttons):
        self.check_buttons = check_buttons
        self.selected_object = BaseObject

    def update(self, event):
        from simulator.engine import lower_bound
        from simulator.interface import positions, active_object
        from simulator.object_classes.medium import remove_point, medium

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and
                coordinate_pixels_to_units(array(event.pos))[1] <= lower_bound):
            for check_button in self.check_buttons.values():
                check_button.activated = False
        if (type(active_object) == medium.Medium and remove_point.RemovePoint in self.check_buttons and len(
                active_object.boundaries) == 3):
            self.check_buttons[remove_point.RemovePoint].activated = False

        previous_selected_object = self.selected_object
        self.selected_object = BaseObject
        for obj, check_button in self.check_buttons.items():
            check_button.update(event)
            if check_button.activated:
                self.selected_object = obj

        if (type(active_object) == medium.Medium and len(active_object.boundaries) == 3 and
                self.selected_object == remove_point.RemovePoint):
            self.check_buttons[self.selected_object].activated = False
            self.selected_object = previous_selected_object
        if self.selected_object != BaseObject:
            self.check_buttons[self.selected_object].activated = True
        if previous_selected_object != self.selected_object:
            positions.clear()

    def draw(self):
        for check_button in self.check_buttons.values():
            check_button.draw()
