#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais,
#o aumento é de 15%.
sal = float(input('Qual seu salário? '))
if sal > 1250:
    print('Terá 10% de aumento totalizando R${}'.format((sal * 10 / 100) + sal))
else:
    print('Terá 15% de aumento totalizando R${}'.format((sal * 15 / 100) + sal))
