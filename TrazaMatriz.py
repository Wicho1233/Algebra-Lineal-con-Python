import numpy as np 
from numpy.linalg import eig
#Traza de una matriz
#La traza (tr) de una matriz A se obtiene al sumar los elementos de la diagonal principal de la matriz A, para ello, es necesario que la matriz A sea cuadrada, 
# de orden nxn, es decir, que la matriz A debe tener un número de renglones igual al número de columnas
A= np.array([[1,0,6,9], [-1,3,6,4],[3,-1,6,3],[1,5,6,-1]])
#Atravez de la funcion trace se resuelve la tarza de la matriz A
result = np.trace(A)
print(result)
