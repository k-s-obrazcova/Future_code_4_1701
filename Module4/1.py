class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year_create = year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year_create} y."


class Library:
    books = []

    @staticmethod
    def add_book(book):
        Library.books.append(book)

    @staticmethod
    def remove_book(title):
        Library.books = [book for book in Library.books if book.title != title]

    @staticmethod
    def find_books(title):
        found_books = [book for book in Library.books if title.lower() in book.title.lower()]
        return found_books

    @staticmethod
    def total_books():
        return len(Library.books)

    @staticmethod
    def save_to_file(filename):
        with open(filename, 'w') as file:
            for book in Library.books:
                file.write(f"{book.title}, {book.author}, {book.year_create}\n")


book_first = Book("First", "Kseniia", 2024)
book_second = Book("Second", "Anonim", 1978)
book_third = Book("Summer", "Alex F.", 2003)

Library.add_book(book_first)
Library.add_book(book_second)
Library.add_book(book_third)

print(Library.total_books())

found = Library.find_books("e")
for book in found:
    print(book)

Library.save_to_file("library.txt")
