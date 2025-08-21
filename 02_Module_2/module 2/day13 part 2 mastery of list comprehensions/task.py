print("mini task 1")
lists = [5, 10, 15, 20]
result = ["yes" if num % 10 == 0 else "no" for num in lists]
print(result)

print("\nMini task 2")
matrix = [[2, 4], [6, 8 ], [10,12]]
even = [[n/2 for n in row]for row in matrix]
print(even)

print("\nChallenge 1")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result= [num ** 2 for row in matrix for num in row if num%2 != 0]
print(result)

print("\nnext-challenge: reverse vowel only")
words = ["hello", "world", "python", "guru"]
rev = [word[::-1] for word in words]
print(rev)

print("\nactual task")
words = ["apple", "sky", "orange", "banana", "grape"]
rev= [word[::-1] for word in words if word[0] not in "aeiou" ]
print(rev)

print("\nchallenge final")
nested = [[1, 2, 3], [4, 5, 6], [7]]

dou = [num + num for row in nested for num in row if num % 2!= 0]
print(dou)