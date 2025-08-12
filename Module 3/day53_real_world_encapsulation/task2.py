class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            return "Password updated successfully."
        else:
            return "Error: Password must be at least 6 characters."


user = UserProfile("hari@example.com", "password123")

print(user.set_password("123456"))
print(user.set_password("123"))
