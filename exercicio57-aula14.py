#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # strip() remove espaços, upper() coloca em maiusculas, [0]utiliza apenas a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))







'''fiz o exemplo abaixo '''
'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite M para masculino ou F para feminino: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print('Opção selecionada com SUCESSO!!!')
    else:
        print('Opção INVÁLIDA, digite novamente!')
print('FIM')'''
