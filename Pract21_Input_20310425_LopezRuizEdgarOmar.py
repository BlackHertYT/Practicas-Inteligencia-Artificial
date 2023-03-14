# -*- coding: utf-8 -*-
"""


@author: Omar
"""

edad = int(input('¿Cuál es tu edad?\n'))

if edad <= 0:
	print('Eres muy chico como para poder usar la compu')

elif edad >= 1 and edad < 18:
	print('Eres un chavalon.')

elif edad >= 18 and edad < 45:
	print('Ojo, ve contratando un paquete funerario.')

elif edad >= 45 and edad <100:
    print('Ya caducaste mi hermano')

elif edad > 100 and edad <=120:
    print('Probablemente estes en un museo')

else:
	print('Edad no válida.')