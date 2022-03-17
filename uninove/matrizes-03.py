import numpy as np

matriz01 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,20,30]])
matriz02 = np.array([[2,2,2], [6,9,-10], [1,7,9] , [3,6,8]])
matriz03 = np.zeros((1,3))
matrizresultante = np.concatenate((matriz01,matriz02,matriz03))

print("Matriz 01")
print(matriz01)
 
print("Matriz 02")
print(matriz02)
 
print("Matriz 03")
print(matriz03)
 
print("Matriz Concetenada")
print(matrizresultante)
