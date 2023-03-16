# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#El programa define una tupla llamada colores que contiene cuatro elementos de tipo string: 'rojo', 'azul', 'verde' y 'amarillo'. Luego, utiliza un ciclo for para iterar sobre cada elemento de la tupla, guardándolo temporalmente en la variable x. 
colores = ('rojo','azul','verde','amarillo')

#Dentro del ciclo, se imprime en pantalla un mensaje que incluye el valor de x, concatenando el string "El color es: " al inicio y el string "." al final. Al ejecutar el programa, se imprimirá en pantalla cuatro mensajes, uno para cada elemento de la tupla, indicando que "El color es" seguido del nombre del color correspondiente.
for x in colores:
    print("El color es: "+x+".")
