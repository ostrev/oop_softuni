from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 > self.maximum:
            self.speed = self.maximum
        else:
            self.speed += 2



    @property
    def maximum(self):
        return 120
