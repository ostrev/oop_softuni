from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTest(TestCase):
    def setUp(self) -> None:
        self.truck = TruckDriver('Tosho', 10)

    def test_init(self):
        t = TruckDriver('Tosho', 100)
        self.assertEqual(t.name, "Tosho")
        self.assertEqual(t.money_per_mile, 100)
        self.assertEqual(t.available_cargos, {})
        self.assertEqual(t.earned_money, 0)
        self.assertEqual(t.miles, 0)

    def test_earned_money_correct(self):
        self.truck.earned_money = 1
        self.assertEqual(1, self.truck.earned_money)

    def test_earned_money_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.truck.earned_money = -1
        self.assertEqual(f"Tosho went bankrupt.", str(ex.exception))

    def test_earned_money_zero(self):
        self.truck.earned_money = 0
        self.assertEqual(0, self.truck.earned_money)

    def test_add_cargo_that_is_in_dict(self):
        self.truck.available_cargos = {'Sofiq': 250, 'Varna': 450}
        with self.assertRaises(Exception) as ex:
            self.truck.add_cargo_offer('Sofiq', 20)
            self.truck.add_cargo_offer('Varna', 250)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_correct(self):
        self.truck.add_cargo_offer('Sofiq', 250)
        self.truck.add_cargo_offer('Varna', 450)
        self.assertEqual({'Sofiq': 250, 'Varna': 450}, self.truck.available_cargos)
        self.assertEqual('Cargo for {cargo_miles} to {cargo_location} was added as an offer.', self.truck.add_cargo_offer())
    def test_drive_best_cargo_offer_rais_error(self):
        self.assertEqual("There are no offers available.", self.truck.drive_best_cargo_offer())

    def test_drive_best_cargo_offer_rais_error2(self):
        self.assertEqual("There are no offers available.", self.truck.drive_best_cargo_offer())

    def test_drive_best_cargo_offer_no_activity2(self):
        self.truck.add_cargo_offer('Varna', 150)
        self.assertEqual('Tosho is driving 150 to Varna.', self.truck.drive_best_cargo_offer())
        self.assertEqual(1500, self.truck.earned_money)
        self.assertEqual(150, self.truck.miles)


    def test_drive_best_cargo_offer_no_activity(self):
        self.truck.add_cargo_offer('Sofiq', 100)
        self.truck.add_cargo_offer('Varna', 150)
        self.assertEqual('Tosho is driving 150 to Varna.', self.truck.drive_best_cargo_offer())
        self.assertEqual(1500, self.truck.earned_money)
        self.assertEqual(150, self.truck.miles)

    def test_drive_best_cargo_offer_no_activity_same_miles(self):
        self.truck.add_cargo_offer('Sofiq', 150)
        self.truck.add_cargo_offer('Varna', 150)
        self.assertEqual('Tosho is driving 150 to Sofiq.', self.truck.drive_best_cargo_offer())
        self.assertEqual(1500, self.truck.earned_money)
        self.assertEqual(150, self.truck.miles)

    def test_drive_best_cargo_offer_no_activity_have_miles(self):
        self.truck.miles = 10
        self.truck.add_cargo_offer('Sofiq', 100)
        self.truck.add_cargo_offer('Varna', 150)
        self.assertEqual('Tosho is driving 150 to Varna.', self.truck.drive_best_cargo_offer())
        self.assertEqual(1500, self.truck.earned_money)
        self.assertEqual(160, self.truck.miles)

    def test_drive_best_cargo_offer_activity(self):
        self.truck.add_cargo_offer('Sofiq', 100)
        self.truck.add_cargo_offer('Varna', 30000)
        self.assertEqual('Tosho is driving 30000 to Varna.', self.truck.drive_best_cargo_offer())
        self.assertEqual(263750, self.truck.earned_money)
        self.assertEqual(30000, self.truck.miles)
        self.assertEqual(10, self.truck.money_per_mile)

    def test_activity_no_change(self):
        self.truck.check_for_activities(5)
        self.assertEqual(0, self.truck.earned_money)

    def test_activity_eat_change_no_money_error(self):
        with self.assertRaises(ValueError) as ex:
            self.truck.check_for_activities(250)
        self.assertEqual(f"Tosho went bankrupt.", str(ex.exception))

    def test_activity_eat_change_have_money(self):
        self.truck.earned_money = 500
        self.truck.miles = 249
        self.truck.check_for_activities(250)
        self.assertEqual(480, self.truck.earned_money)

    def test_eat(self):
        self.truck.earned_money = 100
        self.truck.eat(250)
        self.assertEqual(80, self.truck.earned_money)

    def test_sleep(self):
        self.truck.earned_money = 100
        self.truck.sleep(250)
        self.assertEqual(100, self.truck.earned_money)

    def test_sleep2(self):
        self.truck.earned_money = 100
        self.truck.sleep(1000)
        self.assertEqual(55, self.truck.earned_money)

    def test_pump_gas(self):
        self.truck.earned_money = 500
        self.truck.pump_gas(1500)
        self.assertEqual(0, self.truck.earned_money)


    def test_repair_truck(self):
        self.truck.earned_money = 10000
        self.truck.repair_truck(10000)
        self.assertEqual(2500, self.truck.earned_money)

    def test_repr(self):
        self.truck.miles = 234
        self.assertEqual("Tosho has 234 miles behind his back.", self.truck.__repr__())

    def test_activity_30000(self):
        self.truck.earned_money = 150000
        self.truck.check_for_activities(30000)
        self.assertEqual(113750, self.truck.earned_money)

if __name__ == '__main__':
    main()
