from math import sqrt, floor #aqui é iportado apenas a função de raiz e arredondamento pra baixo
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
