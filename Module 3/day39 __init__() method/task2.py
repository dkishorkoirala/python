class User:
    def __init__(self,username, email):
        self.username = username
        self.email = email
        
    def show_info(self):
        print(f"User {self.username} can be contacted at {self.email}")
        
u1 = User("Hari", "b7aHk@example.com")
u2 = User("Ram", "ram@example.com")

u1.show_info()
u2.show_info()