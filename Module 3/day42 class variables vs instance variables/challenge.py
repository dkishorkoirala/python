class Library:
    total_books_created = 0

    def __init__(self, book_name):
        self.book_name = book_name
        Library.total_books_created += 1


b1 = Library("The alchemist")
print("Total Books created:", Library.total_books_created)

b2 = Library("Rich Dad and Poor Dad")
print("Total Books created:", b2.total_books_created)
