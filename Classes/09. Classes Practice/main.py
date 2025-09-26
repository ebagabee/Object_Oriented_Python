class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        mantain_books = []

        for item in self.books:
            if item.title is not book.title or item.author is not book.author:
                mantain_books.append(item)

        self.books = mantain_books
            

    def search_books(self, search_string):
        search_list = []
        search_term = search_string.lower()
    
        for item in self.books:
            if search_term in item.title.lower() or search_term in item.author.lower():
                search_list.append(item)

        return search_list
