from time import sleep
print('-==-'*7)
print('CALCULANDO NOTAS DOS ALUNOS')
print('-==-'*7)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('CALCULANDO A NOTA... AGUARDE!')
sleep(2)
if m < 5:
    print('A média do aluno ficou em {:.1f}, portanto foi REPROVADO!'.format(m))
elif m >= 7:
    print('A média do aluno fcou em {:.1f}, portanto foi APROVADO!'.format(m))
else:
    print('A média do aluno ficou em {:.1f}, portanto está em RECUPERAÇÃO!'.format(m))