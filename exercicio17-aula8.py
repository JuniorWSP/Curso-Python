'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.'''
from math import sqrt
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print('A hipotenusa desses valores é {:.3f}'.format(sqrt((co**2)+(ca**2))))

'''from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.3f}'.format(hi))'''
