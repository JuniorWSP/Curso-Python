#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
#final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO,
#Média 7.0 ou superior: APROVADO.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Que pena. Sua nota é {} e você está REPROVADO!'.format(m))
elif m < 6.9:
    print('Sua nota é {} estude um pouco mais. Você está em RECUPERAÇÃO!'.format(m))
else:
    print('PARABENS!!!, sua nota é {} e está APROVADO!!!'.format(m))
