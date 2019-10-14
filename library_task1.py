# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
# Book class and adds the book to books list for current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
# the specified author
# - group_by_year(year: int) - returns a list of all books grouped by the
# specified year

# All 3 classes must have a readable __repr__ method!

# Also, book class should have a class variable which holds the amount of
# all existing books


class Library:
    def __init__(self, name, books=None, authors=None):
        self.name = name
        self.books = books or []
        self.authors = authors or []

    def new_book(self, book):
        self.books.append(book)

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        pass


class Book:

    books_amount = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        Book.books_amount += 1


class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books


lib1 = Library('Fiction')
auth1 = Author('Orwell', 'UK', 'June 25th', ['1984', 'Animal farm'])
book1 = Book('1984', 1960, auth1)

lib1.new_book(book1)

print(lib1.books)
print(lib1.group_by_author('Orwell'))