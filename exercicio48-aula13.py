#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
#que se encontram no intervalo de 1 até 500.
print('A soma dos números ímpares e múltiplo de 3 é: ')
soma = 0
for impar in range(501):
    if (impar % 3 == 0):
        if (impar % 2 == 1):
            soma = soma + impar
print(soma)
