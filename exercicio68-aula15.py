#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
#jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')


'''from random import randint
print('=' * 25)
print('Vamos jogar PAR ou ÍMPAR')
print('=' * 25)
valor = int(input('Diga um valor: '))
parIm = str(input('Você quer Par ou Ímpar? [P/I] ')).strip().upper()[0]
pc = randint(0, 10)
soma = pc + valor
if soma % 2 == 0:
    resultado = 'PAR'
else:
    resultado = 'ÍMPAR'
print(f'Você jogou {valor} e o computador {pc}. Total deu {soma} que É {resultado}')
if parIm in 'Pp':
    if resultado == 'PAR':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
elif parIm in 'Ii':
    if resultado == 'ÍMPAR':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
'''
