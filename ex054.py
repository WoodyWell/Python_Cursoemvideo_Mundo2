from datetime import date
atual = date.today().year
contn = 0
contv = 0
nasc = 0
for c in range (1, 8):
    nasc = int(input('Digite em que ano a {}º pessoa nasceu: '.format(c)))
    if nasc > atual:
        print('Essa pessoa ainda não nasceu!')
    elif atual - nasc >= 21:
        contv += 1
    elif atual - nasc < 21:
        contn += 1
print('Ao todo tivemos {} pessoas maiores de idade.\n'
      'E também tivemos {} pessoas menores de idade.'.format(contv, contn))
