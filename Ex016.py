import math
n = float(input('Digite um número:'))
r = math.floor(n)
print('O valor digitado foi {} e a sua proção inteira é {}.' .format(n,r))

'''ou'''
from math import trunc

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, trunc(num))) 

'''ou'''

number = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(number, int(number)))