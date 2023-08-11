c = 1
cont = 0
num = 0
while True:
    num = int(input('Escolha um número para ver a tabuada: '))
    if num < 0:
        break
    print('='*40)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
        c += 1
print('Programa finalizado pois foi digitado um número negativo.')
