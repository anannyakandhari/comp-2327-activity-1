"""
Description: A class to manage LibraryItem objects.
"""
_author_ = "Amanpreet Kaur"
_version_ = "1.0.0"



from genre.genre import Genre


class LibraryItem:
    def __init__(self, item_id, title, author, genre, is_borrowed=False):
        # Validate item_id (must be an integer)
        if not isinstance(item_id, int):
            raise ValueError("item_id must be an integer")

        # Validate title (cannot be blank)
        if not title.strip():
            raise ValueError("title cannot be blank")

        # Validate author (cannot be blank)
        if not author.strip():
            raise ValueError("author cannot be blank")

        # Validate genre (must be a Genre enum)
        if not isinstance(genre, Genre):
            raise ValueError("genre must be a valid Genre")

        # Validate is_borrowed (must be a boolean)
        if not isinstance(is_borrowed, bool):
            raise ValueError("is_borrowed must be a boolean")

        # Assign attributes
        self.item_id = item_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = is_borrowed
