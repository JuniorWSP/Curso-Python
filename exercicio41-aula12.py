#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
#atleta a mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM, Até 14 anos: INFANTIL,
#Até 19 anos: JUNIOR, Até 20 anos: SÊNIOR, Acima: MASTER.
from datetime import date
ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} anos e vai para categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e vai para categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e vai para categoria JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem {} anos e vai para categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e vai para categoria MASTER.'.format(idade))

