#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
#a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar
#ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
media = 0
soma = 0
quant = 0
maior = menor = 0
while resp in 'Ss':     #enquanto resp estiver em S ou s
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(num, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
