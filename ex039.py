from datetime import date
print('-==-'*7)
print('VERIFICAÇÃO DE ALISTAMENTO')
print('-==-'*7)
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nasc
ali = nasc + 17
fal = ali - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))
if fal > 1:
    print('Ainda faltam {} anos para o alistamento.\n'
          'Previsão de alistamento: {}'.format(fal, ali))
elif fal == 0:
    print('Você deve se alistar esse ano! Atenção!')
else:
    fal2 = ano - ali
    print('Você já deveria ter se alistado há {} anos. \n'
          'Ano de alistamento: {}'.format(fal2, ali))
