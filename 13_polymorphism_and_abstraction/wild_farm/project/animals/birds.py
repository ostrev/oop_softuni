from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_INCREMENTAL = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    WEIGHT_INCREMENTAL = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

