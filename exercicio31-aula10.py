#Desenvolva um programa que pergunte a distância de uma viagem de Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dist = float(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    print('O valor da viagem é de {:.2f}'.format(dist * 0.5))
else:
    print('O valor da viagem é de {:.2f}'.format(dist * 0.45))
