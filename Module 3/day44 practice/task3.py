class Library:
    all_titles = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Library.all_titles.append(title)


b1 = Library("Gita", "Vyasa")
b2 = Library("Ramayana", "Valmiki")
print(Library.all_titles)
