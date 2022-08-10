import numpy as np
A = np.array([[2, -1], [3, 2]])
B = np.arange(1, 10)
B = B.reshape(3, 3)
for i in range(3):
    B[i][i] = i
print(B)

