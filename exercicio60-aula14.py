#Faça um programa que leia um número qualquer e mostre seu fatorial.
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))


'''from math import factorial
n = int(input('Digite um número para calcular o seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}'.format(n, f))
'''

'''fat = int(input('Digite um número: '))
f = 1
fatorial = fat
while fat > 1:
    f = f * fat
    fat = fat - 1
print('O fatorial de {} é {}'.format(fatorial, f))'''
