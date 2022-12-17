from project.core.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_name_two(value, "Name cannot be an empty string!")
        self.__name = value

    def sort_drivers(self):
        return sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)