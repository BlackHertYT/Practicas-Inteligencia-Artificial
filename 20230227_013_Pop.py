# -*- coding: utf-8 -*-
"""


@author: Omar
"""
#Este programa crea una lista llamada "numeros" que contiene diez cadenas de texto.
numeros = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'cero']
#Luego, se crea una lista vacía llamada "numerospop" con dos elementos.
#A continuación, se utiliza la función "pop" para eliminar el elemento 'dos' de la lista "numeros" y se almacena en la posición 0 de la lista "numerospop".
numerospop=['','']
#Luego, se utiliza de nuevo la función "pop" para eliminar el elemento 'cero' de la lista "numeros" y se almacena en la posición 1 de la lista "numerospop".
#Finalmente, se utiliza la función "print" para imprimir la lista "numerospop", que contiene los elementos 'dos' y 'cero' en ese orden.
numerospop[0] = numeros.pop(1)
numerospop[1] = numeros.pop(8)
print(numerospop)
