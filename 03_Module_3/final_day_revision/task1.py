class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}")


b1 = Book("The Alchemist", "Paulo Coelho")
b1.info()
