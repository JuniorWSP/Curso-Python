#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
#os espaços. Ex: pode ser lido de traz pra frente.
frase = str(input('Digite uma frase: ')).strip().upper()   #strip retira os espaços, upper coloca maiuscula
palavras = frase.split()    #divide as palavras
junto = ''.join(palavras)   #junta as palavras
inverso = ''
for letra in range (len(junto) -1, -1, -1): #fez-se o inverso indo da ultima letra ate a primeira voltando uma letra
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')