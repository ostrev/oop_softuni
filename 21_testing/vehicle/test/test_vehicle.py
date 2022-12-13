from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTest(TestCase):
    def setUp(self) -> None:
        fuel = 50
        capacity = fuel
        horse_power = 150
        fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.vehicle = Vehicle(fuel, horse_power)

    def test_init(self):
        self.assertEqual(50, self.vehicle.fuel, 50)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise_exception_lower_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct_input(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_raise_exception_greater_fuel(self):
        self.vehicle.drive(30)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct_input(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(10)
        self.assertEqual(22.5, self.vehicle.fuel)

    def test_str(self):
        result = f"The vehicle has {self.vehicle.horse_power} " \
                f"horse power with {self.vehicle.fuel} " \
                f"fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, self.vehicle.__str__())

if __name__ == '__main__':
    main()