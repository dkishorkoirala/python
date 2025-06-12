print("mini task")

def total_marks(*args):
    total = 0
    for marks in args:
        total += marks
    return total
    

print(total_marks(85, 90, 78))

print("\nDaily challenge project")
def create_bio(**kwargs):
    for key, value in kwargs.items():
        print (f"{key}: {value}")
    
create_bio(name="Dibash", age=22, skill="Python", dream="AI Engineer")