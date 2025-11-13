import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
diag = np.diag(matrix)
diag_sum = diag.sum()

print("Matrix:\n", matrix)
print("Diagonal:", diag)
print("Diagonal Sum:", diag_sum)
