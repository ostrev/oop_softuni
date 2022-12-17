from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    breathe_units = 10

    def __init__(self, name: str):
        super().__init__(name, 50)
