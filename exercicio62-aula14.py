#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.
termo = int(input('Digite o 1° termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
t = 0
while t < 10:
    print('{}° termo é {}'.format(t + 1, termo))
    termo = termo + razao
    t = t + 1

