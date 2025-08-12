class Account:
    def __init__(self, username, password, login_status):
        self.__username = username
        self.__password = password
        self.__login_status = login_status

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        if len(new_password) >= 8 and any(char.isdigit() for char in new_password):
            self.__password = new_password
            return "Password updated successfully."
        else:
            return "Error: Password must be at least 8 characters and contain a number."

    def login(self, password_attempt):
        if password_attempt == self.__password:
            self.__login_status = True
            return "Login successful!"
        else:
            return "Error: Invalid password."

    def logout(self):
        self.__login_status = False

    def show_status(self):
        if self.__login_status:
            return "Logged in"
        else:
            return "Logged out"


manager = Account("admin", "password123", False)

print(manager.set_password("password1"))
print(manager.set_password("password"))
print(manager.login("password1"))
print(manager.show_status())
manager.logout()
print(manager.show_status())
