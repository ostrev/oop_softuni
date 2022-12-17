from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.helper.creates import Creates
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.create_astronaut = Creates()
        self.list_astronauts_on_space = []
        self.flag_complete = False
        self.count_mission = 0
        self.total_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        try:
            astronaut = self.create_astronaut.create_astronaut(astronaut_type, name)
        except:
            raise Exception("Astronaut type is not valid!")
        if any(a.name == name for a in self.astronaut_repository.astronauts):
            return f"{name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if any(a.name == name for a in self.planet_repository.planets):
            return f"{name} is already added."
        planet = Creates.create_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not any(a.name == planet_name for a in self.planet_repository.planets):
            raise Exception("Invalid planet name!")

        planet = self.planet_repository.find_by_name(planet_name)

        list_ast = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        list_ast_sorted = sorted(list_ast, key=lambda a: a.oxygen, reverse=True)
        if not list_ast_sorted:
            raise Exception("You need at least one astronaut to explore the planet!")

        if len(list_ast_sorted) > 5:
            astronauts_for_mission = list_ast_sorted[:5]
        else:
            astronauts_for_mission = list_ast_sorted
        # send on mission
        self.flag_complete = False
        self.total_mission += 1
        self.list_astronauts_on_space = []
        for _ in range(len(astronauts_for_mission)):
            astronaut_on_mission = astronauts_for_mission.pop(0)
            self.list_astronauts_on_space.append(astronaut_on_mission)

            for _ in range(len(planet.items)):
                item = planet.items.pop()
                astronaut_on_mission.backpack.append(item)
                astronaut_on_mission.breathe()

                if not planet.items:
                    self.flag_complete = True
                    break
                if astronaut_on_mission.oxygen <= 0:
                    break
            if self.flag_complete:
                break
        total_astronauts = self.list_astronauts_on_space + astronauts_for_mission
        if self.flag_complete:
            self.count_mission += 1
            return f"Planet: {planet_name} was explored. {len(self.list_astronauts_on_space)} " \
                   f"astronauts participated in collecting items."
        else:
            return "Mission is not completed."



    def report(self):
        result = ''
        result += f'{self.count_mission} successful missions!\n'
        result += f'{self.total_mission - self.count_mission} missions were not completed!\n'
        result += f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f'Name: {astronaut.name}\n'
            result += f'Oxygen: {astronaut.oxygen}\n'
            items = ', '.join(astronaut.backpack)
            result += f'Backpack items: {items if items else "none"}\n'
        return result


# astronaut = None
        # if astronaut_type == "Biologist":
        #     astronaut = Biologist(name)
        # elif astronaut_type == "Geodesist":
        #     astronaut = Geodesist(name)
        # elif astronaut_type == "Meteorologist":
        #     astronaut = Meteorologist(name)
        # else:
        #     raise Exception("Astronaut type is not valid!")