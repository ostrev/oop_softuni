class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        need_fuel = kilometers * self.DEFAULT_FUEL_CONSUMPTION
        if need_fuel <= self.fuel:
            self.fuel -= need_fuel
