movies = []

for i in range(3):
    m = input("Enter name of movies: ")
    movies.append(m)

file = open ("movies.txt", "w")
for m in movies:
    file.writelines(m + "\n")
file.close()