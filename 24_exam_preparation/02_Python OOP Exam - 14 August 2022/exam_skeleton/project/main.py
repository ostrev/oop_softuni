
from project.horse_race_app import HorseRaceApp
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred


horse1 = Appaloosa("Appaloosa", 115)
horse2 = Thoroughbred("Thoroughbred", 135)
horse2.train()
horse2.train()
horse2.train()
print(horse2.speed)



