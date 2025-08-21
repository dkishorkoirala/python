class Library:
    def __init__(self, books):
        self.books = books if books else []

    def __len__(self):
        return len(self.books)

    def __contains__(self, books):
        return books in self.books

    def __add__(self, other):
        if isinstance(other, Library):
            return Library(self.books + other.books)
        return NotImplemented

    def __str__(self):
        return f"Library({self.books})"


b1 = Library(["the alchemist", "rich dad and poor dad"])
b2 = Library(["harry potter", "miraj"])

b3 = b1 + b2
print(len(b3))
print("harry potter" in b3)
print(b3)
