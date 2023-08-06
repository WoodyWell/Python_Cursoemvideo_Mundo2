from time import sleep
print('-==-'*8)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-==-'*8)
num = int(input('Digite um número inteiro: '))
print('Digite o número correspondente a opção desejada: ')
print('[ 1 ] converter para BINÁRIO \n'
      '[ 2 ] converter para OCTAL \n'
      '[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Escolha uma das opções: '))
print('CALCULANDO... AGUARDE!')
sleep(3)
if escolha == 1:
    print('O número {} convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Você não escolheu uma opção válida! Programa finalizado!')
