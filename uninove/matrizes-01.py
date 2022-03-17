import numpy as np

matriz = np.array([[1,2,3],[4,5,6],[7,8,9],[10,20,30]])

print("Matriz:",matriz)
print("Elemento posicao (1,2):",matriz[1][2])
print("Dimensoes:",matriz.ndim)

matriz[3][1] = 18

print("Matriz:",matriz)
