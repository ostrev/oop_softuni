from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    increment = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)
        self.type = 'SaltwaterFish'

    def eat(self):
        self.size += self.increment
