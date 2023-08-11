print('='*22)
print('Sequência de Fibonacci')
print('='*22)
n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
cont = 3
print(' {} -> {}'.format(termo1, termo2), end='')
while cont <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
