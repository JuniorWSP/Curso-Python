#Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor
#digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-' * 40)
    tab = 0
    while tab <= 10:
        mult = num * tab
        print(f'{num} X {tab} = {mult}')
        tab = tab + 1
    print('=' * 40)
