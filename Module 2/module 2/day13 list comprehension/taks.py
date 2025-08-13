number = [ 1, 2, 3, 4, 5]

squares = [num * num for num in number]
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evennum = [num for num in numbers if num % 2 == 0]
print(evennum)

print("\ntask 1")

numbers = [1, 2, 3, 4, 5, 6]
square_even = [num*num for num in numbers if num % 2 == 0]
print(square_even)

print("\ntask 2")

words = ['apple', 'banana', 'cherry']
first = [letter[0] for letter in words]
print(first)

print("\ntask 3")

words = ["hi", "hello", "python", "is", "fun"]

length = [len(word) for word in words if len(word) > 4 ]
print(length)

print("\nchalenge 1")
words = ["sun", "moon", "sky", "space"]

rev_word = [ word[::-1] for word in words if len(word) % 2 != 0]
print(rev_word)

print("\nchallenge 2")
numbers= [i for i in range(51) if i % 3 == 0  and i % 5 != 0]
print(numbers)

print("\ntask 4")

nums = [1, 3, 5, 7, 9]

great = [ num *num for num in nums if num * num > 20]
print(great)

print("\ntask 5")
word = "beautiful"

wor = [ w for w in word if w != "a" and w != "e" and w!="i" and w != "o" and w != "u"]
print(wor)

print("\nChallenge 3")
nested = [[1, 2], [3, 4], [5]]
new = [j for i in nested for j in i]
print(new)

print("\ntask 6")
a = [1,2,3]
b = [2,3,4]

lists = [(i,j) for i in a for j in b if i < j]
print(lists)

print("\nchallenge 4: ")
word = "chocolate"

new =''.join ([ i for i in word if i not in "aeiou"])[::-1]
print(new)

print("\nchallenge 5")
sentence = "My phone number is 9841234567 and PIN is 1234"

digits = [i for i in sentence if i in "1234567890"]
print(digits)