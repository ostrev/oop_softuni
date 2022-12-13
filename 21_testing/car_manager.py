class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self) -> None:
        make = 'Peugeot'
        model = '407'
        fuel_consumption = 10
        fuel_capacity = 50
        fuel_amount = 0
        self.car = Car(make, model, fuel_consumption, fuel_capacity)

    def test_make_setter_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_correct_make(self):
        self.car.make = "BMW"
        self.assertEqual("BMW", self.car.make)

    def test_model_setter_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_correct_make(self):
        self.car.make = "406"
        self.assertEqual("406", self.car.make)

    def test_fuel_consumption_setter_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_correct_integer(self):
        self.car.fuel_consumption = 8
        self.assertEqual(8, self.car.fuel_consumption)

    def test_fuel_capacity_setter_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test__fuel_capacity_with_correct_integer(self):
        self.car.fuel_capacity = 55

        self.assertEqual(55, self.car.fuel_capacity)

    def test_fuel_amount_setter_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_with_correct_integer(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_that_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_that_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.car.refuel(11)
        self.assertEqual(11, self.car.fuel_amount)
        self.car.refuel(11)
        self.assertEqual(22, self.car.fuel_amount)

    def test_refuel_amount_gt_capacity(self):
        # fuel_capacity = 50
        self.car.refuel(51)
        self.assertEqual(50, self.car.fuel_amount)


    def test_drive_raise_exception(self):
        # fuel_consumption = 10
        # fuel_capacity = 50
        with self.assertRaises(Exception) as ex:
            distance = 100
            self.car.drive(100)
            # needed = (distance / 100) * self.car.fuel_consumption
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_decrease_fuel_amount(self):
        # fuel_consumption = 10
        # fuel_capacity = 50
        self.car.fuel_amount = 11
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)

if __name__ == '__main__':
    main()

