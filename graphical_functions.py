from numpy import array


def units_to_pixels(value):
    from main import screen
    return value * (screen.get_width() / 32)


def pixels_to_units(value):
    from main import screen
    return value / (screen.get_width() / 32)


def coordinate_units_to_pixels(point):
    from main import screen
    return (point / array([16, -9]) + 1) * array([screen.get_width() / 2, screen.get_height() / 2])


def coordinate_pixels_to_units(point):
    from main import screen
    return (point / array([screen.get_width() / 2, screen.get_height() / 2]) - 1) * array([16, -9])
