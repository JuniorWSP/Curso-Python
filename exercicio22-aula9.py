#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
