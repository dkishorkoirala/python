print("mini task 1")

sq = lambda x : x ** 2
print(sq(int(input("Enter any number you want square of: "))))

print("\nmini task 2")
mul = lambda x , y: x * y
print(mul(x = int(input("Enter first number: ")), y = int(input("Enter second number to multiply: ")) ))

print("\nmore: ")
check = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check(int(input("Enter number to check if its even or odd: ")))) 

print("\nsort list of tuples by second element")
t =  [(1, 3), (2, 1), (4, 2)]

sorted_tuple = sorted(t , key= lambda x : x[1])
print("Sorted by second element are:",sorted_tuple)

print("\nBonus Challenge 1: Maximum of Three Numbers")
maximum = lambda x, y, z : x if x > y and x > z else(y if y >z and y>x else z)
print(maximum(x=(int(input("Enter first number to compare: "))), y= int(input("Enter second number to compare: ")), z= int(input("Enter third number to compare: "))))


print("\nbonus challenge 2 : check if year is leap year")
is_leap = lambda year: "Leap Year" if (year % 4 == 0 and year % 100 != 0 ) or (year  % 400 == 0 ) else "Not leap year" 
print(is_leap(year = int(input("enter a year to check: "))))