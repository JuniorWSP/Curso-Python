#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
#da progressão usando a estrutura while.
termo = int(input('Digite o 1° termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
while cont < 10:
    print('{}° termo é {}'.format(cont + 1, termo))
    termo = termo + razao
    cont = cont + 1
print('FIM')
