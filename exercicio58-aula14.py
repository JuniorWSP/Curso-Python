#Melhore o jogo do Desafio 28 onde o computador vai 'pensar' em um número entre 0 a 10.
#Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram
#necessários para vencer.
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pesar em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi? ')
acertou = False   #a variável recebe false porque ainda não foi acertado.
tentativas = 0
while not acertou:   #enquano você não acertou, ou seja fará o enquanto até você acertar.
    jogador = int(input('Qual é o seu palpite? '))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas!!!'.format(tentativas))



'''fiz o exemplo abaixo'''
'''from random import randint
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
        print('NÃO foi esse, tente novamente!!!')'''



