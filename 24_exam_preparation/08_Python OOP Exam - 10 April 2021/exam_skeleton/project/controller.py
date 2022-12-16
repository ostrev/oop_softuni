from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    valid_aquariums_type = ["FreshwaterAquarium", "SaltwaterAquarium"]
    valid_decoration_type = ["Ornament", "Plant"]
    valid_fish_type = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type in self.valid_aquariums_type:
            if aquarium_type == 'FreshwaterAquarium':
                self.aquariums.append(FreshwaterAquarium(aquarium_name))
            else:
                self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type in self.valid_decoration_type:
            if decoration_type == 'Ornament':
                self.decorations_repository.add(Ornament())
            else:
                self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decorator = self.decorations_repository.find_by_type(decoration_type)
        if decorator == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        else:
            for aquarium in self.aquariums:
                if aquarium.name == aquarium_name:
                    aquarium.add_decoration(decorator)
                    self.decorations_repository.remove(decorator)
                    return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type in self.valid_fish_type:
            if fish_type == "FreshwaterFish":
                fish = FreshwaterFish(fish_name, fish_species, price)
            else:
                fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium = None
            for aq in self.aquariums:
                if aq.name == aquarium_name:
                    aquarium = aq
            if aquarium is None:
                return
            if aquarium.capacity == len(aquarium.fish):
                return "Not enough capacity."
            elif aquarium.type != fish_type:
                return "Water not suitable."
            else:
                aquarium.add_fish(fish)
                return f"Successfully added {fish_type} to {aquarium_name}."
        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        count = 0
        aquarium = None
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                aquarium = aq

        if aquarium is not None:
            for fish in aquarium.fish:
                fish.eat()
                count += 1
        return f"Fish fed: {count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = None
        total_sum = 0
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                aquarium = aq
        if aquarium is not None:
            for fish in aquarium.fish:
                total_sum += fish.price
            for dec in aquarium.decorations:
                total_sum += dec.price
            return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += aquarium.__str__()
            result += '\n'
        return result.strip()

#
# # #
# contr = Controller()
# print(contr.add_aquarium('FreshwaterAquarium', 'aqua_1'))
# print(contr.add_aquarium('FreshwaterAquarium', 'aqua_1'))
# print(contr.add_aquarium('SaltwaterAquarium', 'aqua_2'))
# print(contr.add_aquarium('Aquarium', 'aqua_2'))
# print(contr.add_aquarium('SaltwaterAquarium', 'aqua'))
#
# print(contr.add_decoration('Ornament'))
# print(contr.add_decoration('Plant'))
# print(contr.add_decoration('Ornafdfment'))
#
#
# print(contr.insert_decoration('aqua', 'Orndsdment'))
# print(contr.insert_decoration('aqua_1', 'Ornament'))
# print(contr.insert_decoration('aqua_2', 'Ornament'))
# print(contr.insert_decoration('aqua_2', 'Plant'))
#
# print(contr.add_fish('FreshwaterAquarium', 'SerFish', 'riba', 'red', 5))
# print(contr.add_fish('FreshwaterAquarium', 'SerFish', 'riba', 'red', 5))
#
# print(contr.add_fish('aqua_2', 'SaltwaterFish', 'riba', 'red', 5))
# print(contr.add_fish('aqua_2', 'SaltwaterFish', 'riba', 'red', 5))
# print(contr.add_fish('aqua_1', 'SaltwaterFish', 'riba', 'red', 5))
# print(contr.add_fish('aqua_1', 'FreshwaterFish', 'riba', 'red', 5))
# print(contr.add_fish('aqua_1', 'FreshwaterFish', 'riba', 'red', 5))
# print(contr.add_fish('aqua_1', 'FreshwaterFish', 'riba', 'red', 5))
#
#
# print(contr.feed_fish('aqua_1'))
# print(contr.feed_fish('aqua_2'))
# print(contr.feed_fish('aqua'))
# print(contr.report())
#
# print((contr.calculate_value('aqua_1')))
# print((contr.calculate_value('aqua_2')))