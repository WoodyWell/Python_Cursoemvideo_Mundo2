from random import randint
print('Que tal um jogo de advinhação?')
print('Acabei de pensar em um número entre 0 e 10.')
num = randint(0, 10)
cont = 0
resp = int(11)
print('Será que você consegue advinhar? U.u')
print('===='*8)
while resp != num:
    resp = int(input('Qual é o seu palpite? '))
    cont += 1
    if resp > num:
        print('Menos... Tente novamente.')
    if resp < num:
        print('Mais... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(cont))
