# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#Este programa pregunta al usuario su edad y, según el valor de la edad ingresada, muestra un mensaje diferente.
edad = int(input('¿Cuál es tu edad?\n'))
#En primer lugar, el programa convierte la entrada del usuario a un entero y la almacena en la variable 'edad'.
#Luego, el programa evalúa si la edad es menor o igual a cero. Si lo es, imprime un mensaje diciendo que el usuario es muy chico para usar la computadora.
#Si la edad es mayor que cero, el programa procede a evaluar en qué rango de edad se encuentra la persona.
if edad <= 0:
	print('Eres muy chico como para poder usar la compu')
#Si la edad está entre 1 y 17, el programa muestra un mensaje diciendo que es un "chavalon".
elif edad >= 1 and edad < 18:
	print('Eres un chavalon.')
#Si la edad está entre 18 y 44, el programa muestra un mensaje advirtiendo al usuario que debería considerar contratar un paquete funerario.
elif edad >= 18 and edad < 45:
	print('Ojo, ve contratando un paquete funerario.')
#Si la edad está entre 45 y 99, el programa muestra un mensaje diciendo que el usuario ya caducó.
elif edad >= 45 and edad <100:
    print('Ya caducaste mi hermano')
#Si la edad está entre 100 y 120, el programa muestra un mensaje indicando que el usuario probablemente se encuentra en un museo.
elif edad > 100 and edad <=120:
    print('Probablemente estes en un museo')

else:
#Finalmente, si la edad no está en ninguno de estos rangos, el programa muestra un mensaje diciendo que la edad ingresada no es válida.
	print('Edad no válida.')