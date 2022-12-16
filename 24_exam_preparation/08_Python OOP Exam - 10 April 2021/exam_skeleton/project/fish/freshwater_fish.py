from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    increment = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)
        self.type = 'FreshwaterFish'

    def eat(self):
        self.size += self.increment
