#Escreva um programa que faça o coputador "pensar" em um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
#escrever na tela se o usuário venceu ou perdeu.

from random import randint   #randomiza um número inteiro
pc = randint(0, 5)   #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Digite um número: '))   #jogador tenta adivinhar
if jogador == pc:
    print('Parabéns! Você advinhou.')
else:
    print('Você errou, eu pensei no número {} e não no número {}'.format(pc, jogador))
