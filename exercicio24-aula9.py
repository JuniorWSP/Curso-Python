#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".
cidade = str(input('Diga o nome de uma cidade: ')).strip()
print("Ela começa com a palavra Santo?", cidade[:5].upper() == 'SANTO')
