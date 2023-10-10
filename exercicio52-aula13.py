#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))
if(n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0):
    print('NÃO!!! O número {} não é primo.'.format(n))
else:
    print('SIM!!! O número {} é primo.'.format(n))
