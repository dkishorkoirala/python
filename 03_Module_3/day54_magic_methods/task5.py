class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    def __len__(self):
        return len(self.title)


book1 = Book("The Alchemist", "Paulo Coelho")

if print(str(book1)) == print(book1):
    print(True)
else:
    print(False)
# print(repr(book1))
# print(len(book1))
print()
print(book1)
print(repr(book1))
