class User:
    def __init__(self, username):
        self.username = username

    def display_user(self):
        print(f"User: {self.username}")


class AdminUser(User):
    def show_permission(self):
        print("Has full access")


u1 = AdminUser("Rambilas")
u1.display_user()
u1.show_permission()
