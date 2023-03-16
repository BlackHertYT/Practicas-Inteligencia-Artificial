# -*- coding: utf-8 -*-
"""


@author: Omar
"""

#Este programa define tres pares de variables numéricas (num1 y num2, num3 y num4, y num5 y num6) y utiliza la estructura condicional "if" para imprimir un mensaje en caso de que se cumpla una determinada afirmación.
num1 = 35
num2 = 50

#En el primer bloque "if", se verifica si num1 es diferente de num2. Si se cumple esta condición, se imprime el mensaje "Si se cumple la afirmación 1".
if num1 != num2:
	print('Si se cumple la afirmacion 1')
    
num3 = 89
num4 = 55

#En el segundo bloque "if", se verifica si num3 es mayor que num4. Si se cumple esta condición, se imprime el mensaje "Si se cumple la afirmación 2".
if num3 > num4:
	print('Si se cumple la afirmacion 2')
    
num5 = 67
num6 = 67


#En el tercer bloque "if", se verifica si num5 es diferente de num6. Como num5 y num6 tienen el mismo valor, esta condición no se cumple y el mensaje "Si se cumple la afirmación 3" no se imprime.
if num5 != num6:
	print('Si se cumple la afirmacion 3')