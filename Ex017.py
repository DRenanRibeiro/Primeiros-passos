ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
hip= (((ca**2) + (co**2))**(1/2))
print('A hipotenusa vai medir {:.2f}' .format(hip))

''' ou '''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))