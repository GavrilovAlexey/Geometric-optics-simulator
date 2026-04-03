from numpy import array
from simulator.interface import update, draw_interface, base_refractive_index_slider
from simulator.object_classes.absorber import Absorber
from simulator.object_classes.ray import Ray

lower_bound = -5
number_of_iterations = 50
error = 10 ** -9
base_refractive_index = 1

objects = [
    Absorber(array([16., 9.]), array([16., -9.])),
    Absorber(array([-16., 9.]), array([16., 9.])),
    Absorber(array([-16., 9.]), array([-16., -9.])),
    Absorber(array([-16., lower_bound]), array([16., lower_bound])),
]


def engine():
    global objects, error, base_refractive_index
    output = update()
    if output != "ok":
        return output

    base_refractive_index = base_refractive_index_slider.value
    for obj in objects:
        obj.update()
    draw_interface()
    for obj in objects:
        if isinstance(obj, Ray):
            obj.draw(number_of_iterations)
        else:
            obj.draw()

    return "ok"
