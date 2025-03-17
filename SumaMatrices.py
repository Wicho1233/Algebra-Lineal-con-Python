import numpy as np
#Declaracion de matrices 
a = np.array([[1,0,6,9], [-1,3,6,4],[3,-1,6,3],[1,5,6,-1]])
b=np.array([[-1,3,4,7], [-2,2,1,5],[1,-2,3,1],[2,2,1,-2]])
#Usando la funcion add para sumar
result = np.add(a,b)
#Imprimir resultado
print(result)