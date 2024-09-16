class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        if isinstance(book, Book):
            if book not in self.books:
                self.books.append(book)
            else:
                return print("Book already exists in database.")
        else:
            return print("Please provide a book in correct format to add it to the library.")

    def remove_book(self, book_title):
        for index, book in enumerate(self.books):
            if book_title in book.title:
                self.books.pop(index)
                return print("Book was removed.")
        return print("Book was not found.")

    def borrow_book(self, book_title):
        for index, book in enumerate(self.books):
            if book_title in book.title:
                self.books.pop(index)
                self.borrow_books.append(book)
                return print("Book was marked as borrowed.")

    def available_books(self):
        list_of_titles = []
        for book in self.books:
            list_of_titles.append(book.title)
        return list_of_titles

    def borrowed_books(self):
        list_of_titles = []
        for book in self.borrow_books:
            list_of_titles.append(book.title)
        return list_of_titles

book1 = Book("Title1", "Author1", 2023)
book2 = Book("Title2", "Author2", 2003)
book3 = Book("Title3", "Author3", 2004)
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.remove_book(book3.title)

library.borrow_book(book2.title)

print(library.available_books())
print(library.borrowed_books())