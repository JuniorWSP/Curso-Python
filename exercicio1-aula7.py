n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {} \n e a divisão é {:.3f}'. format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'. format(di, e))
#o *args: dentro do parenteses o pycharm acrescentou sozinho, ate então não houve problemas com isso
#o \n serve para dar quebra de linha
#o end='' apesar de ter dois prints, seja escrito na mesma linha e não em duas linhas diferentes podendo
#podendo ate colocar algum valor, simbolo ou caractere dentro das ''