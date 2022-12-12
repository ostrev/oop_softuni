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

    
if __name__ == '__main__':
    main()