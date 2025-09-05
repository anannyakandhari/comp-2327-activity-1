"""
Description: A class to manage LibraryItem objects.
Author: Anannya

Version: 1.0.0
"""

from genre.genre import Genre


class LibraryItem:
    """This class represents a library item like a book or DVD."""

    def __init__(self, item_id, title, author, genre, is_borrowed=False):
        # Validate item_id (must be an integer)
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        self.__item_id = item_id

        # Validate title (cannot be blank)
        if not title.strip():
            raise ValueError("Title cannot be blank.")
        self.__title = title.strip()

        # Validate author (cannot be blank)
        if not author.strip():
            raise ValueError("Author cannot be blank.")
        self.__author = author.strip()

        # Validate genre (must be a Genre enum)
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        self.__genre = genre

        # Validate is_borrowed (must be a boolean)
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        self.__is_borrowed = is_borrowed

    # Accessors / Getters
    @property
    def item_id(self):
        """Return the item id."""
        return self.__item_id

    @property
    def title(self):
        """Return the title."""
        return self.__title

    @property
    def author(self):
        """Return the author."""
        return self.__author

    @property
    def genre(self):
        """Return the genre."""
        return self.__genre

    @property
    def is_borrowed(self):
        """Return True if borrowed, False if available."""
        return self.__is_borrowed
