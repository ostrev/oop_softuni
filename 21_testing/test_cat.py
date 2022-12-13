class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False

from unittest import TestCase, main



class CatTest(TestCase):
    def setUp(self) -> None:
        self.cat = Cat('name')

    def test_init(self):
        name = 'Pusi'
        cat = Cat(name)
        self.assertEqual(name, cat.name)
        self.assertEqual(0, cat.size)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)

    def test_eat_fed_is_true(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_fed_is_false(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(1, self.cat.size)
        self.cat.sleep()
        self.cat.fed = False
        self.cat.eat()
        self.assertEqual(2, self.cat.size)

    def test_sleep_fed_is_false(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_fad_is_true(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)

if __name__ == '__main__':
    main()