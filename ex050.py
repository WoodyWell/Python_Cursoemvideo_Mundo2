cont = int(0)
soma = int(0)
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você digitou {} números pares e a soma dos valores é: {}'.format(cont, soma))
