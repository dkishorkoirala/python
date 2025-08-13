class UserProfile:
    def __init__(self, email):
        self.__email = email

    def set_email(self, email):
        if "@" in email:
            self.__email = email
            return "Email updated successfully."
        else:
            return "Error: Invalid email format."


user = UserProfile("hari@example.com")
print(user.set_email("Ram@example.com"))
print(user.set_email("Ramexample.com"))
