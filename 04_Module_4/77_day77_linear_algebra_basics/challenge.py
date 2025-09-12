import numpy as np

ratings = np.array([[5, 4, 0, 1], [4, 0, 0, 1], [1, 1, 0, 5]])

print("Dot product of user1 and user2:\n", np.dot(ratings[0], ratings[1]))
print("Dot product of user1 and user3:\n", np.dot(ratings[0], ratings[2]))

sims = np.dot(ratings, ratings[0])
sims[0] = -1
print("User most similar to user1 is:", np.argmax(sims) + 1)

print("Bonus:")
movies = ratings.T
print("Movie similarity (dot products):\n", np.dot(movies, movies.T))
