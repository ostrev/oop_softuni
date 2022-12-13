from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        name = 'name'
        type = "mammal_type"
        sound = 'sound'
        __kingdom = "animals"
        self.mammal = Mammal(name, type, sound)

    def test_init(self):

        self.assertEqual('name', self.mammal.name)
        self.assertEqual('mammal_type', self.mammal.type)
        self.assertEqual('sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())


    def test_get_kingdom(self):
        self.mammal.get_kingdom()
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())


    def test_info(self):
       self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())

if __name__ == '__main__':
    main()
