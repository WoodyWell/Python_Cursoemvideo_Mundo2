frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
uniao = ''.join(palavras)
inverso = uniao[::-1].upper()
print('O inverso de \033[31m{}\033[m é \033[35m{}\033[m.'.format(uniao, inverso))
if uniao == inverso:
    print('Neste caso, temos um palíndromo!')
else:
    print('Esta frase \033[31mNÃO\033[m é um palíndromo!')
