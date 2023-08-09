num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[35m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('Este é um número PRIMO')
else:
    print('Este \033[31mNÃO\033[m é um número PRIMO')
