#Crie um programa que leia um número Real pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, trunc(n)))

'''n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(n)))'''