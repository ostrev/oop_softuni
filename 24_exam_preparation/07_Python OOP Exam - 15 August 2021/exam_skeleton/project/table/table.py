from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.drink.drink import Drink
from project.drink.water import Water
from project.helpers.validator import Validate


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validate.validation_for_zero_negative(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = sum([f.price for f in self.food_orders])
        drink_bill = sum([d.price for d in self.drink_orders])
        return food_bill + drink_bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        result = ''
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n"
            result += f"Type: {self.__class__.__name__}\n"
            result += f"Capacity: {self.capacity}"
        return result


#
# table_1 = Table(21, 1)
# table_2 = Table(52, 6)
# table_1.reserve(4)
# print(table_1.is_reserved)
# print(table_1.number_of_people)
# table_1.order_food(Bread('white', 4))
# table_1.order_food(Bread('white', 4))
# print(table_1.food_orders)
# table_1.order_drink(Water('juice', 3, 'apple'))
# print(table_1.drink_orders)
# print(table_1.get_bill())
# table_1.clear()
# print(table_1.free_table_info())