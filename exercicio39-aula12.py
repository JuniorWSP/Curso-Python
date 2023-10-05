#Faça um programa que leia o ano e nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai alistar ao serviço militar, Se é a hora de se alistar, Se já passou do tempo do
#alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
prazo = date.today().year - ano
if prazo < 17:
    print('Você tem {} anos, falta {} anos para seu alistamento!'.format(prazo, (17 - prazo)))
elif prazo < 20:
    print('Você tem {} anos, está na hora de se alistar!'.format(prazo))
else:
    print('Você tem {} anos e já passou {} anos do tempo de alistamento'.format(prazo, (prazo - 20)))
