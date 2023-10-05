#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
#normal e condição de pagamento: À vista dinheiro/cheque: 10% de desconto, À vista no cartão: 5% de
#desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.
print('{:-^40}'.format(' Loja do Junior '))
valor = float(input('Digite o valor do produto: R$'))
print('''Diga a forma de pagamento: 
[1] À vista Dinheiro/cheque 
[2] À vista Cartão 
[3] 2x Dividido 
[4] 3x ou mais Parcelado''')
pagamento = int(input('Escolha a opção: '))
dinheiro = valor - (valor * 10 / 100)
cartao = valor - (valor * 5 / 100)
dividido = valor
parcelado = valor + (valor * 20 / 100)
if pagamento == 1:
    print('O valor a ser pago é R${:.2f} já com desconto de 10%.'.format(dinheiro))
elif pagamento == 2:
    print('O valor a ser pago é R${:.2f} já com desconto de 5%.'.format(cartao))
elif pagamento == 3:
    print('O valor a ser pago é R${:.2f} pois não tem desconto.'.format(dividido))
elif pagamento == 4:
    totparc = int(input('Quer dividir em quantas parcelas? '))
    parcelas = parcelado / totparc
    print('O valor total a ser pago será R${:.2f}'.format(parcelado))
    print('Que dará {} parcelas de R${:.2f}, pois terá 20% de juros.'.format(totparc, parcelas))
else:
    print('Opção INVÁLIDA!')
