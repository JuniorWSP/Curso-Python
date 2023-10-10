#Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora
#utilizando um laço for.
n = int(input('Escreva um número: '))
print('A tabuada de {} número é:'.format(n))
for tabuada in range(0, 11):
    resposta = tabuada * n
    print('{} X {} = {}'.format(n, tabuada, resposta))
