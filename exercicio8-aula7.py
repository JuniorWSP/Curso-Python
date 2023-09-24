#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milímetros.
m = float(input('Escreva a medida em metros: '))
print('Valor em centímetros {:.0f}cm e valor em milímetros {}mm'.format(m*100, m*1000))
