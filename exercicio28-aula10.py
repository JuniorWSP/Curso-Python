#Escreva um programa que faça o coputador "pensar" em um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
#escrever na tela se o usuário venceu ou perdeu.

from random import choice
n1 = int(input(0))
n2 = int(input(1))
n3 = int(input(2))
n4 = int(input(3))
n5 = int(input(4))
n6 = int(input(5))
num = [0, 1, 2, 3, 4, 5]
print('Digite um número: '.format(choice(num)))
