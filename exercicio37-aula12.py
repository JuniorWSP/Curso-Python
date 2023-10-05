#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
#será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão: 
[1] converter para Binário 
[2] converter para Octal 
[3] converter para Hexadecimal''')
conversao = int(input('Digite uma opção :'))
if conversao == 1:
    print('{} é o valor em Binário'.format(bin(n)[2:]))
elif conversao == 2:
    print('{} esse valor é Octal'.format(oct(n)[2:]))
elif conversao == 3:
    print('{} esse valor é Hexadecimal'.format(hex(n)[2:]))
else:
    print('Valor base INCORRETO! Escolha 1, 2 ou 3')
