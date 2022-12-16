from project.drink.drink import Drink
from project.drink.tea import Tea


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 1.5, brand)


# """to run this @abstractmethod must be commented"""
#
# drink = Drink('whisky', 100, 10, 'Dimple')
# print(drink.__repr__())
# tea = Tea('black', 250, 'Lipton')
# print(tea.__repr__())
# water = Water('mineral', 1500, 'Devin')
# print(water.__repr__())
#
# drink = Drink('fdfdf', 1, 0, '  ')

