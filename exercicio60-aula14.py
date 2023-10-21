#Faça um programa que leia um número qualquer e mostre seu fatorial.
fat = int(input('Digite um número: '))
f = 1
fatorial = fat
while fat > 1:
    f = f * fat
    fat = fat - 1
print('O fatorial de {} é {}'.format(fatorial, f))
