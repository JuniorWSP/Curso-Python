nome = str(input('Qual é o seu nome? '))
if nome == 'Junior':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Bia Bel Mel':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia {}!'.format(nome))
