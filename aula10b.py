n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média é {:.2f}'.format(m))
if m >= 8:
    print('Uau, bela nota!')
elif m >= 6:
        print('Tá na media!')
elif m >= 4:
        print('Estude mais, sua nota esta baixa!')
else:
    print('Que freio, nota muito ruim!')

