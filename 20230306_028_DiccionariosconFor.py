# -*- coding: utf-8 -*-
"""


@author: Omar
"""
#El programa define dos diccionarios llamados audifono1 y audifono2 con información de diferentes modelos de audífonos.
audifono1 = {
	'Categoría': 'Audifonos',
	'Modelo': 'Samsung Ear buds Pro',
	'Precio': '120,00'
}

audifono2 = {
	'Categoría': 'Audifonos',
	'Modelo': 'Air pods pro',
	'Precio': '160,00'
}
#Luego, el programa recorre las claves del diccionario audifono1 utilizando un bucle for. En cada iteración del bucle, el programa imprime la clave y el valor correspondiente del diccionario audifono1. 
for x in audifono1:
	print(x+" = " +audifono1[x])