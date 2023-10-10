#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
#forem pares. Se o valor digitado for ímpar desconsidere-o.
soma = 0
for num in range(6):
    n = int(input('Digite um número: '))
    if(n % 2 == 0):
        soma = soma + n
print('O somatório dos números pares digitados é {} '.format(soma))
if(soma == 0):
    print('Foi digitado apenas números ímpares.')
