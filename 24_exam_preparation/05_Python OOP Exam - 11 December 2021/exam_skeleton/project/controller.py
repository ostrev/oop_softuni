from project.core.factory import Factory


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.item_factory = Factory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(c.model == model for c in self. cars):
            raise Exception(f"Car {model} is already created!")
        car = self.item_factory.create_car(car_type, model, speed_limit)
        if car is None:
            return
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = self.item_factory.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")
        driver = self.item_factory.create_race(race_name)
        self.races.append(driver)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = [d for d in self.drivers if d.name == driver_name][0]

        car_list_of_correct_type = [c for c in self. cars if c.__class__.__name__ == car_type and c.is_taken is False]
        if not car_list_of_correct_type:
            raise Exception(f"Car {car_type} could not be found!")
        car = car_list_of_correct_type.pop()

        if driver.car is None:
            car.is_taken = True
            driver.car = car
            return f"Driver {driver.name} chose the car {car.model}."
        old_model = driver.car.model
        driver.car.is_taken = False
        driver.car = car
        car.is_taken = True
        return f"Driver {driver.name} changed his car from {old_model} to {car.model}."


    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]

        if not any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][0]

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if any(d.name == driver.name for d in race.drivers):
            return f"Driver {driver.name} is already added in {race.name} race."
        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name: str):
        if not any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} could not be found!")
        race = [r for r in self.races if r.name == race_name][0]

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        list = race.sort_drivers()[:3:]

        for d in list:
            d.number_of_wins += 1

        result = ''
        for d in list:
            result += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.\n"
        return result.strip()