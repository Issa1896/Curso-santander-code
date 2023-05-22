class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def search_books(self, keyword):
        results = []
        for book in self.books:
            if keyword in book.title or keyword in book.author:
                results.append(book)
        return results

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description
