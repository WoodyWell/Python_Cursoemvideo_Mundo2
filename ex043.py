print('-==-'*5)
print('CALCULADORA DE IMC')
print('-==-'*5)
peso = float(input('Digite o seu peso em (Kg): '))
alt = float(input('Digite a sua altura em (m): '))
imc = peso / (alt * alt)
print('O seu IMC é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif imc <= 25:
    print('Você está com o peso IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está com OBESIDADE.')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA.')
