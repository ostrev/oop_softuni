from abc import ABC, abstractmethod

from project.core.validator import Validator


class Car(ABC):
    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.validate_model(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.validate_speed_range(value, self.min_speed, self.max_speed,
                                       f"Invalid speed limit! Must be between {self.min_speed} and {self.max_speed}!")
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_speed(self):
        pass

    @property
    @abstractmethod
    def max_speed(self):
        pass
