from project.bookstore import Bookstore
from unittest import TestCase, main


class BookTest(TestCase):
    def setUp(self) -> None:
        self.book = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.book.books_limit)
        self.assertEqual({}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book.total_sold_books)

    def test_books_limit_prop_raise_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.book.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(ex.exception))

    def test_books_limit_prop_raise_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.book.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid", str(ex.exception))

    def test_book_limit_correct(self):
        self.book.books_limit = 5
        self.assertEqual(5, self.book.books_limit)

    def test_len_correct_count(self):
        self.book.availability_in_store_by_book_titles['Kniga'] = 5
        self.book.availability_in_store_by_book_titles['Dan'] = 3
        self.assertEqual(8, self.book.__len__())

    def test_len_correct_count_zero_books(self):
        self.assertEqual(0, self.book.__len__())

    def test_receive_book_not_enough_space(self):
        with self.assertRaises(Exception) as ex:
            self.book.receive_book('Braun', 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_have_enough_space_title_not_in(self):
        self.book.receive_book('Braun', 8)
        self.assertEqual({'Braun': 8}, self.book.availability_in_store_by_book_titles)

    def test_receive_book_have_enough_space_title_in(self):
        self.book.receive_book('Braun', 8)
        self.book.receive_book('Braun', 1)
        self.assertEqual({'Braun': 9}, self.book.availability_in_store_by_book_titles)

    def test_receive_book(self):
        self.assertEqual("8 copies of Braun are available in the bookstore.", self.book.receive_book('Braun', 8))

    def test_sell_book_is_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.book.sell_book('Braun', 11)
        self.assertEqual("Book Braun doesn't exist!", str(ex.exception))

    def test_sell_book_is_available_no_copies(self):
        self.book.receive_book('Braun', 8)
        with self.assertRaises(Exception) as ex:
            self.book.sell_book('Braun', 9)
        self.assertEqual("Braun has not enough copies to sell. Left: 8", str(ex.exception))

    def test_sell_book(self):
        self.book.receive_book('Braun', 8)
        self.assertEqual("Sold 7 copies of Braun", self.book.sell_book('Braun', 7))
        self.assertEqual({'Braun': 1}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(7, self.book.total_sold_books)

    def test_str(self):
        self.book.receive_book('Braun', 8)
        self.book.sell_book('Braun', 7)
        self.assertEqual("Total sold books: 7\nCurrent availability: 1\n - Braun: 1 copies", self.book.__str__())
if __name__ == '__main__':
    main()
