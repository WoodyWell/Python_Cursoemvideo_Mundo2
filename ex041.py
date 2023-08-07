import datetime
from datetime import date
print('-==-'*6)
print('CLASSIFICANDO ATLETAS')
print('-==-'*6)
nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    cla = 'MIRIM'
elif idade > 9 and idade <= 14:
    cla = 'INFANTIL'
elif idade > 14 and idade <= 19:
    cla = 'JÚNIOR'
elif idade > 19 and idade <= 25:
    cla = 'SÊNIOR'
elif idade > 25 and idade <= 50:
    cla = 'MASTER'
elif idade > 50:
    cla = 'APOSENTADO'
print('Classificação: {}'.format(cla))
