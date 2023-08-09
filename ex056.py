soma = float()
idade = 0
velhoi = 0
velhon = str()
cont = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        velhoi = idade
        velhon = nome
    if sexo == 'M' and idade > velhoi:
        velhoi = idade
        velhon = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print('A média de idade do grupo é de {:.2f} anos'.format(soma / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velhoi, velhon))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))
