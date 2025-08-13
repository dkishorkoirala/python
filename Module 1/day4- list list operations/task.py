movie_list = ["titanic", "inception", "interstellar", "the dark knight", "the lord of the rings"]

print(movie_list[2])

movie_list[0] = "leonardo de caprio"
print(movie_list)

movie_list.append("titanic")

movie_list.insert(1, "Spiderman")

movie_list.remove("leonardo de caprio")

removed_movie= movie_list.pop()
print(removed_movie)

print(len(movie_list))

print(movie_list[0:3])

for movie in movie_list:
    print(movie.upper())


print("------------Challenge----------------")
grocery_item = []

for i in range(5):
    item = input(f"Enter grocery item {i+1}: ")
    grocery_item.append(item)

print(grocery_item)

remove_item = input("Enter item to remove: ")

if remove_item in grocery_item:
    grocery_item.remove(remove_item)
    print(f"The item {remove_item} has been removed from the list")
else:
    print(f"{remove_item} is not found in your list.")

print("Final Glocery item list: ")
for item in grocery_item:
    print(f"- {item}")