#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
#forem pares. Se o valor digitado for ímpar desconsidere-o.
soma = 0
cont = 0
for num in range(1, 7):
    n = int(input('Digite o {}° número: '.format(num)))
    if(n % 2 == 0):
        soma = soma + n
        cont = cont + 1
print('O somatório dos {} números pares digitados é {} '.format(cont,soma))
if(soma == 0):
    print('Foi digitado apenas números ímpares.')
