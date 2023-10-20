#Melhore o jogo do Desafio 28 onde o computador vai 'pensar' em um número entre 0 a 10.
#Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram
#necessários para vencer.
from random import randint
pc = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-' * 20)
q = 0
while True:
    n = int(input('Digite um número: '))
    q = q + 1
    if n == pc:
        print('CORRETO, eu pensei no {}'.format(pc))
        print('Você acertou na {}° tentativa!'.format(q))
        break
    else:
        print('NÃO foi esse, tente novamente!!!')



