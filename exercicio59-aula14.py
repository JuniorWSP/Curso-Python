#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar,  [2] multiplicar, [3] maior, [4] novos números,  [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))
print('''Selecione uma opção abaixo: 
    [1] para SOMAR
    [2] para MULTIPLICAR
    [3] para MAIOR
    [4] para NOVOS NÚMEROS
    [5] para SAIR DO PROGRAMA''')
print('-=-' * 20)
opcoes = 0
while opcoes != 5:
    opcoes = int(input('Digite a opção escolhida: '))
    if opcoes == 1:
        soma = pv + sv
        print('A soma entre {} + {} é {}'.format(pv, sv, soma))
        break
    elif opcoes == 2:
        produto = pv * sv
        print('A multiplicação entre {} x {} é {}'.format(pv, sv, produto))
        break
    elif opcoes == 3:
        if pv > sv:
            print('{} é maior que {}'.format(pv, sv))
        elif sv > pv:
            print('{} é maior que {}'.format(sv, pv))
        break
    elif opcoes == 4:
        print('Informe os números novamente!')
        pv = int(input('Digite o primeiro valor: '))
        sv = int(input('Digite o segundo valor: '))
    elif opcoes == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!!!')
    print('-=-' * 20)
    sleep(2)
print('FIM do programa! Volte sempre!!!')
