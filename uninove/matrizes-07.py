import numpy as np

matriz = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print ("matriz antes do reshape")
print(matriz)
print("Reshape")
print(matriz.reshape(5,3));
print ("matriz após reshape")
print(matriz)
print("Efetuar resize")

matriz.resize(8,2)

print("Matriz após resize")
print(matriz)
