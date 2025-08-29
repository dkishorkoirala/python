import numpy as np

mat = np.arange(1, 17).reshape(4, 4)
print(mat)

fancy = mat[[0, 0, 3, 3], [0, 3, 0, 3]]
print(fancy)

odd_num = mat[mat % 2 != 0]
print(odd_num)
