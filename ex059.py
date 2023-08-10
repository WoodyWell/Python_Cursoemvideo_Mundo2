num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
resultado = int(0)
escolha = int(0)
while escolha != 5:
    print('\n'
          '\033[31m[ 1 ] soma\033[m\n'
          '\033[32m[ 2 ] multiplicar\033[m\n'
          '\033[33m[ 3 ] maior\033[m\n'
          '\033[34m[ 4 ] novos números\033[m\n'
          '\033[35m[ 5 ] sair do programa\033[m'
          '\n')
    escolha = (int(input('>>>>> Qual opção você deseja? ')))
    print('')
    if escolha == 1:
        resultado = num1 + num2
        print('\033[31mRESULTADO --> A soma entre {} e {} é: {}\033[m'.format(num1, num2, resultado))
        print('-==-'*10)
    if escolha == 2:
        resultado = num1 * num2
        print('\033[32mRESULTADO --> A multiplicação entre {} e {} é: {}\033[m'.format(num1, num2, resultado))
        print('-==-'*10)
    if escolha == 3:
        if num1 > num2:
            print('\033[33mRESULTADO --> O número {} é maior do que o número {}.\033[m'.format(num1, num2))
            print('-==-' * 10)
        elif num2 > num1:
            print('\033[33mRESULTADO --> O número {} é maior do que o número {}.\033[m'.format(num2, num1))
            print('-==-' * 10)
        elif num1 == num2:
            print('\033[33mRESULTADO --> Os dois números são iguais.\033[m')
            print('-==-' * 10)
    if escolha == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print('-==-'*10)
    if escolha != 1 != 2 != 3 !=4 and escolha != 5:
        print('Opção inválida! Tente novamente!')
print('Programa finalizado. Obrigado.')