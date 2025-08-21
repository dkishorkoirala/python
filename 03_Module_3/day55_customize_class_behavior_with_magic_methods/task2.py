class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __eq__(self, value):
        if not isinstance(value, Book):
            return NotImplemented
        return self.pages == value.pages

    def __lt__(self, value):
        if not isinstance(value, Book):
            return NotImplemented
        return self.pages < value.pages

    def __gt__(self, value):
        if not isinstance(value, Book):
            return NotImplemented
        return self.pages > value.pages

    def __str__(self):
        return f"Title: {self.title}, Pages: {self.pages}"


book1 = Book("Book1", 100)
book2 = Book("Book2", 200)

print(len(book1))
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 == "Not a book")
print(book1)
