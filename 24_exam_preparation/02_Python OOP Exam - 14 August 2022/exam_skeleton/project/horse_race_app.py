from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    valid_type_of_hors = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type not in self.valid_type_of_hors.keys():
            return
        horse = self.__class__.valid_type_of_hors[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        if not any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        horse = None
        for h in range(len(self.horses) - 1, -1, -1):
            if not self.horses[h].is_taken and self.horses[h].__class__.__name__ == horse_type:
                horse = self.horses[h]
                break
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} could not be found!")
        race = [r for r in self.horse_races if r.race_type == race_type][0]

        if not any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = [j for j in self.jockeys if j.name == jockey_name][0]

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} could not be found!")
        race = [r for r in self.horse_races if r.race_type == race_type][0]

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        list_participants = sorted(race.jockeys, key=lambda jock: jock.horse.speed, reverse=True)

        winner = list_participants[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

