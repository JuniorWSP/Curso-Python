#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('Os números pares entre 1 e 50 são:')
for pares in range(1, 51):
    if (pares % 2 == 0):
        print(pares, end=' ')
print('ACABOU!!!')


for cont in range(2, 51, 2):   #Dessa forma é melhor pois exige menos desempenho do computador
    print(cont, end=' ')
print('ACABOU!!!')
