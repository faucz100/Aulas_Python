while True:
    n = float(input('Digite um valor: '))
    n1 = float(input('Digite o segundo valor: '))
    print('O que voce deseja fazer com esses valores?')
    print('[1] SOMAR')
    print('[2] SUBTRAIR')
    print('[3] MULTIPLICAR')
    print('[4] DIVIDIR')
    print('[5] SAIR')

    escolha = int(input('Faça sua escolha: '))
    
    if escolha == 5:
        break
    
    elif escolha == 1:
        s = n + n1
        print(f'{n} + {n1} = {s}')
    
    elif escolha == 2:
        s = n - n1
        print(f'{n} - {n1} = {s}')
    
    elif escolha == 3:
        s = n * n1
        print(f'{n} * {n1} = {s}')
    
    elif escolha == 4:
        if n1 == 0:
            print('Não se divide por 0')
        else:
            s = n / n1
            print(f'{n} / {n1} = {s}')
    
    else:
        print('Você digitou errado, digite novamente.')