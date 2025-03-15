import numpy as np
#EJEMPLO
# Supongamos que A es una matriz de n × m y B es una matriz de m×l,ambas matrices con entradas complejas,
a = np.array([[1,0,6,1], [-1,3,6,4],[3,-1,6,3],[1,0,6,-1] ])
b=np.array([[2,3,4,-1],[0,1,-2,3],[-5,3,4,8],[1,-9,3,8]])
result = np.dot(a,b)
print(result)

