class UserProfile:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Error: Password must be at least 6 characters.")

    def display(self):
        print(f"Username: {self.username}")
        print(f"Current Password: {self.__password}")


user = UserProfile("Dibash", "123456")

user.display()
user.set_password("mysecretpass")
user.set_password("pass")
user.display()
