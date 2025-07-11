def power(base):
    def num(n):
        return n ** base
    return num

def divide(a, b):
    if b == 0 :
        return "Couldn't be divided by zero"
    else:
        return a/b
    
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True