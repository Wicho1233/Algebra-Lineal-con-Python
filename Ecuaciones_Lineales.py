from sympy import symbols,Eq,solve
#declaracion de simbolos dependendo del numero de variables
x1,x2=symbols('x1 x2')
#Declaracion de ecuaciones con Eq esta dependera del numero de ecuaciones
eq1 = Eq(3*x1+x2,120)
eq2 = Eq(x1+2*x2,90)
#Manera de resolverla con la funcion solve agregando las ecuaciones y las variables
solucion = solve((eq1,eq2),(x1,x2))
#Impresion de la solucionf
print(solucion)









