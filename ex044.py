print('======== LOJAS WELL ========')
print('-==-'*7)
print('GERENCIADOR DE PAGAMENTOS')
print('-==-'*7)
preco = float(input('Preço total das compras: R$'))
print('FORMAS DE PAGAMENTO:\n'
      '[ 1 ] à vista em dinheiro\n'
      '[ 2 ] à vista no cartão de crédito\n'
      '[ 3 ] 2x no cartão de crédito\n'
      '[ 4 ] 3x no cartão de crédito')
escolha = int(input('Escolha uma das opções: '))
if escolha == 1:
    precofinal = preco - preco * 0.10
    print('Comprando à vista no dinheiro você receberá um desconto de 10%\n'
          'A sua compra no valor de R${:.2f} ficará R${:.2f} com o desconto aplicado'.format(preco, precofinal))
elif escolha == 2:
    precofinal = preco - preco * 0.05
    print('Comprando à vista no cartão de crédito você receberá um desconto de 5%\n'
          'A sua compra no valor de R${:.2f} ficará R${:.2f} com o desconto aplicado'.format(preco, precofinal))
elif escolha == 3:
    precofinal = preco / 2
    print('Comprando em 2x no cartão de crédito não tem juros\n'
          'Você vai pagar 2x de R${:.2f}'.format(precofinal))
elif escolha == 4:
    parc = int(input('Escolha a quantidade de parcelas: '))
    precoj = preco + preco * 0.20
    precofinal = precoj / parc
    print('Comprando em 3x ou mais parcelas você terá 20% de juros\n'
          'Sua compra será parcelada em {} vezes de R${:.2f}\n'
          'A compra de R${:.2f} vai custar R${:.2f}'.format(parc, precofinal, preco, precoj))
else:
    print('Opção INVÁLIDA de pagamento.')
