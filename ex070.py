print('==='*10)
print('LOJAS WELL'.center(30))
print('==='*10)
menor = float()
escolha = ' '
cont = tot1000 = total = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    total += preco
    cont += 1
    if cont == 1:
        menor = preco
        nomemenor = produto
    if preco >= 1000:
        tot1000 += 1
    if menor > preco:
        menor = preco
        nomemenor = produto
    if escolha == 'N':
        break
print('==='*10)
print('FIM DO PROGRAMA'.center(30))
print('==='*10)
print(f'O total das compras foi: R${total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} custando R${menor:.2f}')
