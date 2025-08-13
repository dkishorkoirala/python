class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def check_password(self, input_pass):
        if input_pass == self.__password:
            return "Password match: True"
        else:
            return "Password match: False"


user = UserProfile("user@example.com", "123456")

print(user.check_password("123456"))
print(user.check_password("123457"))
