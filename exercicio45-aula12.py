#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções: 
[1] para PEDRA 
[2] para PAPEL 
[3] para TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 20)
print('O computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 20)
if pc == 0:   #O computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Você Venceu')
    elif jogador == 2:
        print('O computador Venceu')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:   #O computador jogou Papel
    if jogador == 0:
        print('O computador Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você Venceu')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:   #O computador jogou Tesoura
    if jogador == 0:
        print('Você Venceu')
    elif jogador == 1:
        print('O computador Venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
