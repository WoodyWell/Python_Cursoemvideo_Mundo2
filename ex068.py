from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, totalizando {total}.')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if jogada == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif jogada == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO! Você venceu {vitoria} vezes.')
