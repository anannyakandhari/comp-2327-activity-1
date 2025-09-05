"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Anannya"
__version__ = "1.0"

"""
Unit tests for the LibraryItem class.
Run in terminal using:
    python -m unittest tests/test_library_item.py
"""

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre


class TestLibraryItem(unittest.TestCase):

    def test_blank_title_raises_exception(self):
        """Check if a blank title raises ValueError"""
        with self.assertRaises(ValueError):
            LibraryItem(1, "", "Author", Genre.FICTION, False)

    def test_blank_author_raises_exception(self):
        """Check if a blank author raises ValueError"""
        with self.assertRaises(ValueError):
            LibraryItem(1, "Book Title", "", Genre.FICTION, False)

    def test_invalid_genre_raises_exception(self):
        """Check if invalid genre raises ValueError"""
        with self.assertRaises(ValueError):
            LibraryItem(1, "Book Title", "Author", 123, False)

    def test_item_id_not_integer_raises_exception(self):
        """Check if item_id is not an integer"""
        with self.assertRaises(ValueError):
            LibraryItem("one", "Book Title", "Author", Genre.FICTION, False)

    def test_is_borrowed_not_boolean_raises_exception(self):
        """Check if is_borrowed is not a boolean"""
        with self.assertRaises(ValueError):
            LibraryItem(1, "Book Title", "Author", Genre.FICTION, "yes")

    def test_valid_data_sets_attributes(self):
        """Check if valid input correctly sets attributes"""
        item = LibraryItem(1, "Book Title", "John", Genre.FICTION, False)
        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.title, "Book Title")
        self.assertEqual(item.author, "John")
        self.assertEqual(item.genre, Genre.FICTION)
        self.assertFalse(item.is_borrowed)


if __name__ == "__main__":
    unittest.main()
