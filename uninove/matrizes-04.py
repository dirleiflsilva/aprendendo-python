import numpy as np

matriz01 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,20,30]])
matrizresultante = np.split(matriz01,2)

print("Matriz 01")
print(matriz01)
 
print("Matriz Resultante parte 1")
print(matrizresultante [0])
 
print("Matriz Resultante parte 2")
print(matrizresultante [1])
