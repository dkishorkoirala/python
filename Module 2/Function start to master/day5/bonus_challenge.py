print("Bonus-challenge 1: secret funciton vault")
#build a function fet_toolbox() that returns a dictionary of secret tools.


def get_toolbox():
    def square(n): return n * n
    def cube(n): return n ** 3
    def double(n): return n * 2

    return {
        "square": square,
        "cube": cube,
        "double": double
    }
tools = get_toolbox()

print("Square of 4:", tools["square"](4) )   
print("Cube of 3:", tools ["cube"](3))       
print("Double of 6:", tools["double"] (6))  

print("\nBonus challenge: 2 Custom message maker")
#goal : build message_maker(style) that returns a different formatted based on input.

def message_maker(style):
    def loud(msg): return msg.upper() + "!!!"
    def soft(msg): return msg.lower() 
    def title(msg): return msg.title()

    if style == "loud":
        return loud
    elif style == "soft":
        return soft
    elif style == "title":
        return title
    else:
        return lambda msg: msg
    
msg = message_maker("title")
print(msg("Hello world"))

print("\nbonus challenge 3: multi-operation engine")
def build_engine(operation):
    def add_all(lst): return sum (lst)
    def mul_all(lst): 
        result = 1
        for i in lst:
            result *= i
        return result 
    if operation == "add": return add_all
    elif operation == "mul": return mul_all

engine = build_engine("mul")
print(engine([2,3,4]))

print("\nBonus Challenge 4: History Function")
#Build a calculator that returns the result and also keeps history internally.

def smart_calculator():
    history = []
    def calc(op, a, b):
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        else:
            result = None
        
        history .append((op, a, b, result))
        return result
    def show_history():
        return history
    return calc, show_history

use_calc, get_history = smart_calculator()
print(use_calc("add", 3, 4))
print(use_calc("mul", 2, 5))
print(get_history())