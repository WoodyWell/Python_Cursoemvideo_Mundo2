from time import sleep
print('-==-'*9)
print('Análise de financiamento de Imóvel')
print('-==-'*9)
imovel = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos você deseja financiar? '))
prestacao = imovel / (anos * 12) #Valor total do imóvel dividido pela quantidade de anos * 12 meses
limitesalario = salario * 0.30
print('CALCULANDO FINANCIAMENTO...')
sleep(3)
print('Para pagar um imóvel no valor de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(imovel, anos, prestacao))
if prestacao > limitesalario:
    print('A presstação excedeu o limite de 30% do seu salário! FINANCIAMENTO NEGADO')
else:
    print('Após análise o seu financiamento foi APROVADO! PARABÉNS!')
