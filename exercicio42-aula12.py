#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, ESCALENO: todos
#os lados diferentes.
l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))
if (l1 < l2 + l3) and (l2 < l3 + l1) and (l3 < l1 + l2):
    print('Com essas medidas se forma um Triângulo.')
    if (l1 == l2 == l3):
        print('Esse é um triângulo Equilátero.')
    elif (l1 == l2) or (l2 == l3) or (l3 == l1):
        print('Esse é um triângulo Isósceles.')
    else:
        print('Esse é um triângulo Escaleno.')
else:
    print('Não é possível formar um triângulo com essas medidas!')
