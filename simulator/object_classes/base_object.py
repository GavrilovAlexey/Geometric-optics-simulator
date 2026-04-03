class BaseObject:
    required_number_of_points = -1
    @staticmethod
    def create(positions):
        return BaseObject()

    def check(self, position):
        return 0

    def update(self):
        pass

    def distance(self, ray):
        return 0

    def new_ray(self, ray):
        return BaseObject()

    def get_widgets(self):
        return []