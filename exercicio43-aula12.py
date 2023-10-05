#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
#status, de acordo com a tabela abaixo: Abaixo de 18,5: Abaixo do peso, Entre 18,5 e 25: Peso ideal,
#25 ate 30: Sobrepeso, 30 ate 40: Obesidade, Acima de 40: Obesidade mórbida.
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print(imc)
if imc < 18.5:
    print('Você esta abaixo do peso.')
elif imc < 25:
    print('Seu peso está ideal.')
elif imc <= 30:
    print('Você esta com sobrepeso.')
elif imc <= 40:
    print('Você esta com obesidade.')
elif imc > 40:
    print('Você esta com obesidade mórbida.')
