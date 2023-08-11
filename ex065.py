teste = 'S'
cont = soma = maior = menor = 0
while teste in 'Ss':
    num = int(input('Digite um número: '))
    teste = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menos = num
print('Você digitou {} números e a média foi de: {:.1f}'.format(cont, soma / cont))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))
