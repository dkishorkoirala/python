print("mini challenge 1")

words = ["apple", "sky", "banana", "hi", "cherry", "ice"]

word_list = [word[::-1] for word in words if len(word) >= 5]
print(word_list)

print("\nmini challenge 2")
numbers = [11, 4, 7, 2, 9, 6]

new = [i * i for i in numbers if i % 2 == 0]
print(new)

print("\nmini challenge 3")

sentence ="I have 2 cats and 3 dogs. Room number is 404."

num = [i for i in sentence if i in "0123456789"]
print(num)

print("\nmini challenge 4")

a = [1, 2]
b = [10, 20, 30]

mul = [i * j for i in a for j in b]
print(mul)

print("\nmini challenge 5")
sentence = "My friend Alice and Bob Went to Nepal"

caps = [i[0] for i in sentence.split() if i[0].isupper() ]
print(caps)