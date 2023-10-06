n = int(input('Digite um número: '))    #Dessa forma ele irá contar de 0 ate o número digitado.
for cont in range(0, n + 1):
    print(cont)
print('FIM')

inicio = int(input('Inicio: ')) #Dessa forma ele vai pular (passo) do início ate chegar ao final.
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for cont in range(inicio, fim + 1, passo):
    print(cont)
print('FIM')

for cont in range(0, 3):   #Dessa forma é pedido para digitar um valor 3 vezes como nesse caso
    n = int(input('Digite um valor: '))
print('Fim')

s = 0   #Dessa forma ele faz um somatório de todos os numeros digitados nesse caso 4 vezes.
for cont in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores foi {}'.format(s))
