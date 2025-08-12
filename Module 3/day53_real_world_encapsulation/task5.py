class UserProfile:
    def __init__(self, email):
        self.__email = email

    def update_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
            return "Email updated successfully."
        else:
            return "Error: Invalid email format."


user = UserProfile("user@example.com")

print(user.update_email("Ram@example.com"))
print(user.update_email("Ramexample.com"))
