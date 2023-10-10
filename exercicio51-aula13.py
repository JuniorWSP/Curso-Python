#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
#No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao   #formula matemática que calcula o enezimo termo de uma PA
for pa in range(termo, decimo + razao, razao):
    print('{}'.format(pa), end=' -> ')
