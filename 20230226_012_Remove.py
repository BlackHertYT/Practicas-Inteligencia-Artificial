# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#Este programa crea una lista llamada "numeros" que contiene diez cadenas de texto.
numeros = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'cero']
#Luego, se utiliza la función "remove" para eliminar los elementos "dos" y "ocho" de la lista "numeros".
numeros.remove('dos')
numeros.remove('ocho')
#Finalmente, se utiliza la función "print" para imprimir la lista "numeros" actualizada, que contiene los elementos restantes 'uno', 'tres', 'cuatro', 'cinco', 'seis', 'siete' y 'nueve'.
print(numeros)