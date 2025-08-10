# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
