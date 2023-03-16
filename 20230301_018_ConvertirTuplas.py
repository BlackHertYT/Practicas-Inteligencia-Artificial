# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:01:33 2023

@author: guill
"""
#Este programa crea una lista llamada "numeros" que contiene diez cadenas de texto
numeros = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'cero']
#Luego, se utiliza la función "tuple" para crear una tupla llamada "numeros_T" a partir de la lista "numeros".
numeros_T= tuple(numeros)
#Finalmente, se utiliza la función "type" para imprimir el tipo de la variable "numeros_T", que es "<class 'tuple'>". Es decir, que "numeros_T" es una tupla.
print(type(numeros_T))