#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
#se o usuário vai continuar. No final, mostre:
#a) Qual é o total de gasto na compra.
#b) Quantos produtos custam mais de R$1000.
#c) Qual é o nome do produto mais barato.
total = 0
totmil = 0
menorPre = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        totmil = totmil + 1
    if cont == 1:
        menorPre = preco
        barato = produto
    else:
        if preco < menorPre:
            menorPre = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!!!'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorPre:.2f}')
