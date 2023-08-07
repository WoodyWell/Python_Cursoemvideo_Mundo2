print('-==-'*5)
print('COMPARANDO NÚMEROS')
print('-==-'*5)
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
print('VERIFICANDO...')
if num1 > num2:
    print('O PRIMEIRO número é maior.')
elif num2 > num1:
    print('O SEGUNDO número é maior.')
elif num1 == num2:
    print('Os dois números são iguais.')