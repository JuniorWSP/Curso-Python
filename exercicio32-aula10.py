#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date   #importa a data atual
ano = int(input('Digite um ano, ou coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year   #importa a data atual
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('SIM!!! Esse ano de {} é bissexto!'.format(ano))
else:
    print('Esse ano de {} NÃO é bissexto!'.format(ano))
