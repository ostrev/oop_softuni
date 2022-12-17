from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    breathe_units = 5

    def __init__(self, name: str):
        super().__init__(name, 70)
