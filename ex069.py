maiorgeral = 0
qtdhomem = 0
mulhermenor = 0
while True:
    print('==='*7)
    print('CADASTRE UMA PESSOA')
    print('===' * 7)
    idade = int(input('Idade: '))
    if idade >= 18:
        maiorgeral += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo == 'M':
            qtdhomem += 1
        if sexo == 'F':
            if idade < 20:
                mulhermenor +=1
    print('---'*7)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiorgeral}')
print(f'Ao todo foram cadastrados {qtdhomem} homens.')
print(f'Foram cadastradas {mulhermenor} mulheres com menos de 20 anos.')
