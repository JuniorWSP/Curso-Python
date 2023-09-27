#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')))
