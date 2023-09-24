#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('O produto custa: R$'))
print('O preço com desconto será R${}'.format(p-(p*5/100)))
