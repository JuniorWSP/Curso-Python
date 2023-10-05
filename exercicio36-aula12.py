#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
#perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da
#prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))
prestacoes = anos * 12
parcela = valorCasa / prestacoes
print('Isso dará {} prestações de R${} por mes.'.format(prestacoes, parcela))
if parcela <= salario * 30 / 100:
    print('Que BOM!!! você poderá fazer o financiamento.')
    print('As prestações não ultrapassam 30% de sua renda que é de R${}'.format(salario * 30 / 100))
else:
    print('Financiamento NEGADO!')
    print('Financie um valor menor ou aumente o periodo de quitação')
