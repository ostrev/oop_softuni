class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class ListTest(TestCase):
    def setUp(self) -> None:
        self.integer = IntegerList(1, 2, 1.1, '2')

    def test_init_is_empty(self):
        i = IntegerList()
        self.assertEqual([], i._IntegerList__data)

    def test_init_with_strings(self):
        i = IntegerList('1', '2', 4.3)
        self.assertEqual([], i._IntegerList__data)

    def test_init_with_numbs(self):
        self.assertEqual([1, 2], self.integer._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([1, 2], self.integer.get_data())

    def test_add_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer.add('3')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add(self):
        self.integer.add(3)
        self.assertEqual([1, 2, 3], self.integer.get_data())

    def test_remove_index_eq_to_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_gt_of_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.integer.remove_index(1)
        self.assertEqual([1], self.integer.get_data())

    def test_remove_index_return(self):
        self.assertEqual(2, self.integer.remove_index(1))

    def test_get_eq_to_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_gt_of_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_return(self):
        self.integer.get(0)
        self.assertEqual(1, self.integer.get(0))

    def test_insert_index_eq_to_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.insert(2, '1')
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_index_gt_of_len(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.insert(3, '2')
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_index_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.integer.insert(1, '2')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_index(self):
        self.integer.insert(1, 5)
        self.assertEqual([1, 5, 2], self.integer.get_data())

    def test_get_biggest(self):
        self.assertEqual(2, self.integer.get_biggest())

    def test_get_index(self):
        self.assertEqual(1, self.integer.get_index(2))



if __name__ == '__main__':
    main()
