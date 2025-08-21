class Book:
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book '{self.title}' by {self.author} added to collection.")
        
    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class Library():
    def __init__(self):
        self.books= []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                del book
                print(f"Book '{title}' removed from library.")
                return
        print(f"Book {title} not found in lirary")
    
    def show_books(self):
        if not self.books:
            print("Library is empty")
        else:
            print("\nBooks in library")
            for book in self.books:
                print(f"-{book.title}")
                
b1 = Book("1984", "George Orwell", 328)
b2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.show_books()
lib.remove_book("1984")
lib.show_books()