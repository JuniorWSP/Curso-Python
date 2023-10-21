#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
#da progressão usando a estrutura while.
termo = int(input('Digite o 1° termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
t = 0
while t < 10:
    print('{}° termo é {}'.format(t + 1, termo))
    termo = termo + razao
    t = t + 1
