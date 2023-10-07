#Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício,
#indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Contagem Regressiva!!!')
for contador in range(10, 0, -1):
    print(contador)
    sleep(1)
print('BOM, BOM, BOOOOM!!!')
