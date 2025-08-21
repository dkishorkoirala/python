def choose_operation(op):
    def add (a, b): return a+b
    def mul (a,b ): return a * b 

    if op == "add":
        return add
    elif op == "mul":
        return mul
    else:
        return "sorry invalid operation"
operation = choose_operation("add")
print(operation(4, 5))


print("\nchallenge:")
def math_assistant(name):
    def add (a,b): return a+b
    def subtract(a, b ): return a-b
    def multiply (a,b): return a * b
    print(f"Hello {name}, I'm your personal math assistant!")

    return{
        'add' : add,
        'sub' : subtract,
        'mul' : multiply
    }

assistant = math_assistant("Dibash")
print(assistant['add'](4, 5))   
