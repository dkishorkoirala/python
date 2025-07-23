class Movie:
    def __init__(self,title, director, year):
        self.title = title
        self.director = director
        self.year = year
        
    def details(self):
        print(f"Title: {self.title}\nDirector: {self.director}\nYear: {self.year}")

m = Movie("Avatar", "James Cameron", 2009)
m.details()