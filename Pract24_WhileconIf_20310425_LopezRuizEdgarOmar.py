# -*- coding: utf-8 -*-
"""


@author: Omar
"""


x =0
while x <= 30:
    x= x+1
    
    if x != 4 or  x!=6 or x!=10:
        print("El valor  es: " + str(x))
    else:
        print("Se salto el valor de x")
    if x==25:
        break
print("Se salto el bucle cuando x valia: "+str(x))
    