class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.classname = "Book"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        self.classname = "EBook"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        self.classname = "PrintBook"
class Library:
    books = []
    def __init__(self):
        pass
    
    def add_book(self, book):
        Library.books.append(book)
        
    def list_books(self):
        for book in Library.books:
            if book.classname =="PrintBook":
                print(f"{book.classname}: {book.title} by {book.author}, Page count: {book.page_count}")
            elif book.classname == "EBook":
                print(f"{book.classname}: {book.title} by {book.author}, File Size: {book.file_size}")
            elif book.classname == "Book":
                 print(f"{book.classname}: {book.title} by {book.author}")