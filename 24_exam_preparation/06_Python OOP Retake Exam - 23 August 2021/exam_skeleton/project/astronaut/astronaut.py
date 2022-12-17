from abc import ABC, abstractmethod

from project.helper.validate import Validator


class Astronaut(ABC):
    breathe_units = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_names(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.breathe_units

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
    # dali ne e abstrakten
