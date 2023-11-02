#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
#o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
#digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = 0
cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'A soma dos {cont} valores foi {soma}!')


'''num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Foram digitados {cont} e sua soma foi {soma}')'''
