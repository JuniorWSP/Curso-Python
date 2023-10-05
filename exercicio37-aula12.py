#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
#será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.
n = int(input('Escreva um número inteiro: '))
conversao = int(input('Escolha a base para conversão: 1 Binário, 2 Octal, 3 Hexadecimal: '))
binario = n % 2
octal = n
hexadecimal = n
if conversao == 1:
    print('{} é o valor em Binário'.format(binario))
elif conversao == 2:
    print('{} esse valor é Octal'.format(octal))
elif conversao == 3:
    print('{} esse valor é Hexadecimal'.format(hexadecimal))
else:
    print('Valor base INCORRETO! Escolha 1, 2 ou 3')
