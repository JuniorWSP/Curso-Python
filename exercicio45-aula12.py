#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
pc = randint(1, 3)
jogador = int(input('selecione: 1 para PEDRA, 2 para PAPEL ou 3 para TESOURA: '))
print('JO-KEN-PÔ')
if 1 and 2:
    print('Eu escolhi {} e você {}. Papel ganha de Pedra.'.format(pc, jogador))
elif 2 and 3:
    print('Eu escolhi {} e você {}.Tesoura ganha de Papel.'.format(pc, jogador))
elif 1 and 3:
    print('Eu escolhi {} e você {}.Pedra ganha de Tesoura.'.format(pc, jogador))
