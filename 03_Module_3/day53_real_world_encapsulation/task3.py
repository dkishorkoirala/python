class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def display_info(self):
        print(f"Email: {self.__email}", end=" | ")
        print(f"Password: {len(self.__password) * '*'}")


user = UserProfile("user@example.com", "123456")

user.display_info()
