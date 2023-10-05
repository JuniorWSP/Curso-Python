#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
#normal e condição de pagamento: À vista dinheiro/cheque: 10% de desconto, À vista no cartão: 5% de
#desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.
valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Diga a forma de pagamento: 1 Dinheiro, 2 Cartão, 3 Dividido, 4 Parcelado'))
dinheiro = valor - (valor * 10 / 100)
cartao = valor - (valor * 10 / 100)
dividido = valor
parcelado = valor + (valor * 20 / 100)
if pagamento == 1:
    print('O valor a ser pago é R${} com desconto de 10%.'.format(dinheiro))
elif pagamento == 2:
    print('O valor a ser pago é R${} com desconto de 5%.'.format(cartao))
elif pagamento == 3:
    print('O valor a ser pago é R${} pois não tem desconto.'.format(dividido))
elif pagamento == 4:
    print('O valor a ser pago é R${} pois tem acréscimo de 20%.'format(parcelado))
