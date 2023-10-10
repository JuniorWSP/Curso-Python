#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
#que se encontram no intervalo de 1 até 500.
print('A soma dos números ímpares e múltiplo de 3 é: ')
soma = 0
for impar in range(501):
    if (impar % 3 == 0):
        if (impar % 2 == 1):
            soma = soma + impar
print(soma)

res = 0
cont = 0    #BONUS
for c in range(1, 501, 2):   #Outra forma de resolução
    if c % 3 == 0:
        cont = cont + 1     #BONUS, contador geralmente soma + 1
        res = res + c   #acumulador vai se somando, multiplicando, etc.
print('A soma de todos os {} valores solicidados é {}'.format(cont, res))
