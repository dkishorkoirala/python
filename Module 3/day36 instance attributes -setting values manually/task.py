class Book:
    def show_info(self):
        print("\nTitle:", self.title)
        print("Author:", self.author)


book1 = Book()
book2 = Book()
book1.title = "The Alchemist"
book2.title = "The Subtle Art of Not Giving a F*ck"

book1.author = "Paulo Coelho"
book2.author = "Mark Manson"

book1.show_info()
book2.show_info()


class Laptop:
    def method_specs(self):
        print("\nBrand:", self.brand)
        print("Ram Size:", self.Ram_size)


l1 = Laptop()
l2 = Laptop()

l1.brand = "Asus"
l2.brand = "Lenovo"

l1.Ram_size = "8GB"
l2.Ram_size = "16GB"

l1.method_specs()
l2.method_specs()