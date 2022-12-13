from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Audi", "A4", 10, 60)

    def test_correct_initialization(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A4", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_change_make_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_change_make_with_correct_make(self):
        self.car.make = "BMW"

        self.assertEqual("BMW", self.car.make)

    def test_change_model_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_change_model_with_correct_model(self):
        self.car.model = "320"

        self.assertEqual("320", self.car.model)

    def test_change_fuel_consumption_with_zero_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_change_fuel_consumption_with_negative_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_change_fuel_consumption_with_correct_integer(self):
        self.car.fuel_consumption = 8

        self.assertEqual(8, self.car.fuel_consumption)

    def test_change_fuel_capacity_with_zero_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_change_fuel_capacity_with_negative_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_change_fuel_capacity_with_correct_integer(self):
        self.car.fuel_capacity = 55

        self.assertEqual(55, self.car.fuel_capacity)

    def test_change_fuel_amount_with_negative_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_change_fuel_amount_with_correct_integer(self):
        self.car.fuel_amount = 10

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_zero_integer(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_correct_integer(self):
        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_with_biggest_integer_from_capacity(self):
        self.car.refuel(100)

        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_without_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_correct_fuel_amount(self):
        self.car.refuel(60)
        self.car.drive(50)

        self.assertEqual(55, self.car.fuel_amount)


if __name__ == '__main__':
    main()