from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, 245, price)




# bread = Bread('white', 3)
# cake = Cake('banana', 34.4)
# print(bread.__repr__())
# print(cake.__repr__())
