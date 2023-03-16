# -*- coding: utf-8 -*-
"""


@author: Omar
"""

# Se define la variable "string1" con el valor "Hola".
string1 = "Hola"
# Se define la variable "string2" con el valor "Mundo".
string2 = "Mundo"
# Se define la variable "string3" como la concatenación de "string1", un espacio en blanco y "string2".
string3 = string1 + " " + string2
# Se imprime el valor de la variable "string3".
print(string3)

# Se redefine la variable "string1" como la concatenación de la antigua "string1", un espacio en blanco y "string2".
string1 = string1 + " " + string2
# Se imprime el valor de la variable "string1".
print(string1)

# Se imprime la concatenación de las cadenas "Hola ", "Mundo" y "Arriba papito Musk".
print("Hola " + string2 + " Arriba papito Musk")
