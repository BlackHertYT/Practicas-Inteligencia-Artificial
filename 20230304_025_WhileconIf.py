# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#Este programa es un bucle while que va a contar desde 0 hasta 30 y va a imprimir cada número en el camino. Sin embargo, hay algunas condiciones especiales que se aplican a los números 4, 6 y 10, y el bucle se detendrá cuando llegue a 25.
x =0

#Dentro del bucle, primero se incrementa el valor de x en 1. Luego, se evalúa si x no es igual a 4 o no es igual a 6 o no es igual a 10. Si se cumple esta condición, se imprimirá "El valor es:" seguido del valor de x. Si x es igual a 4, 6 o 10, se imprimirá "Se salto el valor de x". Si x es igual a 25, se detiene el bucle con la sentencia break.
while x <= 30:
    x= x+1
    
    
    if x != 4 or  x!=6 or x!=10:
        print("El valor  es: " + str(x))
    else:
        print("Se salto el valor de x")
    if x==25:
        break
print("Se salto el bucle cuando x valia: "+str(x))
    