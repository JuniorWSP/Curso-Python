import math #aqui é importado toda a biblioteca de math
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #math.sqrt vai informar a raiz quadrada do num
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #math.ceil faz o resultado ser arredondado pra cima
