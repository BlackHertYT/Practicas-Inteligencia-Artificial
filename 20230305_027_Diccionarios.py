# -*- coding: utf-8 -*-
"""


@author: Omar
"""
#El programa define dos diccionarios de audífonos, cada uno con información sobre el modelo, la categoría y el precio.
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

#Luego, la información del modelo del audífono 1 se almacena en la variable 'consulta'.
consulta = audifono1['Modelo']
#Finalmente, se imprimen el modelo y el precio del audífono 2.
print(audifono2['Modelo'])
print(audifono2['Precio'])