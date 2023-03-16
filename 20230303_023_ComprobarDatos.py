# -*- coding: utf-8 -*-
"""


@author: Omar
"""

numeros = [1, 2, 3, 4]  # Creamos una lista con los números del 1 al 4

entrada = input('Escribe un numero del 1 al 4 ...\n')  # Pedimos al usuario que ingrese un número

if int(entrada) in numeros:  # Convertimos la entrada a un entero y comprobamos si está en la lista
    print('El numero ' + entrada + ' está dentro de los valores')
else:
    print('El numero ' + entrada + ' no está dentro de los valores')  # Si no está, imprimimos un mensaje de error
