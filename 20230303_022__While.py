# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#El programa utiliza el ciclo while para ejecutar diferentes bloques de código mientras se cumpla una determinada condición:
x=0
#En la primera parte del programa, se inicializa la variable x en cero y se va incrementando en 3 en cada iteración hasta que llega a 30. En cada iteración, se imprime el valor de x.

while x <30:
    x = x+3
    print(x)
print("")

#En la segunda parte del programa, se inicializa la variable x en 20 y se va decrementando en 2 en cada iteración hasta que llega a cero. En cada iteración, se imprime un mensaje concatenado con el valor actual de x.
x=0

while x >-200:
    x = x-10
    print(x)
print("")
#En la tercera parte del programa, se inicializa la variable x en cero y se va decrementando en 10 en cada iteración hasta que llega a -200. En cada iteración, se imprime el valor actual de x.
x=20

while x > 0:
    x = x-2
    print("El valor es "+str(x))