#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))
total = 0
for contador in range(1, n + 1):
    if n % contador == 0:
        print('\033[32m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(contador), end=' ')
print('\n\033[36mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('Esse número É PRIMO!!!')
else:
    print('Esse NÂO é um número primo!!!')
