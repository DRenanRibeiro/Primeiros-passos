from gettext import instal
import math

import emoji as emoji
from numpy import var
import pip

n= int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz de {} é igual a {:.2f}' .format(n, raiz))
print('A raiz de {} é igual a {}' .format (n, math.ceil(raiz)))

#ou
#from math import sqrt
#raiz = sqrt(n)

import random

num = random.random()
print(num)