def mul(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
print(mul(1,2,3,4,5,6))

def prof(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
prof(name = "John", age = 30, city = "New York")