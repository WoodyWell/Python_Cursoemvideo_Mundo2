print('-==-'*6)
print('Analisador de Triângulos')
print('-==-'*6)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r2 + r1:
    print('Os segmentos acima NÃO podem formar um triângulo.')
elif r1 == r2 and r2 == r3:
    print('Este é um triângulo EQUILÁTERO pois todos os lados são iguais.')
elif r1 == r2 and r2 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
    print('Este é um triângulo ISÓSCELES pois possui dois lados iguais e um diferente.')
elif r1 != r2 and r2 != r3:
    print('Este é um triângulo ESCALENO pois todos os lados são diferentes.')
