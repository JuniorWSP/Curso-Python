#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
from math import sin, cos, tan, radians
a = float(input('Digite um valor de ângulo: '))
print('O ângulo {} possui um valor de {:.3f} seno, {:.3f} cosseno e {:.3f} tangente'
      .format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
