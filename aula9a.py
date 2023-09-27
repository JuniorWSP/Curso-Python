frase = 'Curso em Vídeo Python'
print(frase) #escreve toda a frase
print(frase[3]) #escerve apenas o 3° espaço
print(frase[3:13]) #escreve do 3° espaço ate o 12°
print(frase[:13]) #escreve do inicio ate o 13° espaço
print(frase[13:]) #escreve do 13° espaço ate o final
print(frase[3:13:2]) #escreve do 3° espaço ate o 12°
print(frase[::3]) #escreve os espaços pulando de 3 em 3 do início ate o final
print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum auctor, odio at aliquet 
ullamcorper, neque metus eleifend sapien, in euismod odio ante ac metus. Suspendisse potenti. Fusce 
laoreet tincidunt velit, quis cursus dui feugiat sit amet. In auctor tellus vel nisi congue, nec 
pellentesque erat scelerisque. Integer id metus vitae augue ultricies tristique. Vivamus auctor orci 
non ante lacinia, vel aliquet tortor feugiat. Quisque faucibus odio vel nunc malesuada, at lobortis 
nulla elementum.  Proin eget dolor vel tellus egestas iaculis. Nulla facilisi. In lacinia bibendum quam, 
eget mattis dui iaculis eu. Fusce a scelerisque purus.''')
#utilizando 3 aspas ''' no início e no final pode-se escrever um texto inteiro dentro de um único
#print sem a necessicade de repetir um print para cada linha.