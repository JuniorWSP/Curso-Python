#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma
#área de 2m².
l = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
a = l * h
print('A área da parede é {}m e a quantidade de tinta gasta será {}l'.format(a, a/2))
