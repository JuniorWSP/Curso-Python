#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar,  [2] multiplicar, [3] maior, [4] novos números,  [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
menu = ('Somar', 'Multiplicar', 'Maior', 'Novos Números', 'Sair do Programa')
pv = float(input('Digite o primeiro valor: '))
sv = float(input('Digite o segundo valor: '))
print('''Selecione uma opção abaixo: 
[1] para SOMAR
[2] para MULTIPLICAR
[3] para MAIOR
[4] para NOVOS NÚMEROS
[5] para SAIR DO PROGRAMA''')
print('-=-' * 20)
opcoes = int(input('Digite a opção escolhida: '))
n = 0
m = 0
while n != 5:
    if opcoes == 1:
        s = pv + sv
        print('A soma entre {} e {} é {}'.format(pv, sv, s))
        break
    elif opcoes == 2:
        m = pv * sv
        print('A multiplicação entre {} e {} é {}'.format(pv, sv, m))
        break
    elif opcoes == 3:
        if pv > sv:
            print('{} é maior que {}'.format(pv, sv))
            break
        else:
            print('{} é maior que {}'.format(sv, pv))
            break
    elif opcoes == 4:
        pv = float(input('Digite o primeiro valor: '))
        sv = float(input('Digite o segundo valor: '))
        break
    else:
        print('Fim do programa!!!')
        break
