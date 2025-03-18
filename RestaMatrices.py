
import numpy as np
#Declaracion de matrices
a = np.array([[1,0,6,9], [-1,3,6,4],[3,-1,6,3],[1,5,6,-1]])
b=np.array([[-1,3,4,7], [-2,2,1,5],[1,-2,3,1],[2,2,1,-2]])

#Resta de matrices con la funcion substract
result = np.subtract(b,a)
#Impresion del resultado
print(result)
