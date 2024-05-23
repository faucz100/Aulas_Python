while True:
    n = float (input('Digite um valor'))
    n1 = float (input('Digite o segundo valor'))
    print ('''O que voce deseja fazer com esses valores?
           [1]SOMAR
           [2]SUBTRAIR
           [3]MULTIPLICAR
           [4]DIVIDIR
           [5]SAIR''')
    escolha = str (input('Faça sua escolha '))
    if escolha == 5:
        break
    elif escolha == 1:
        s = n + n1
        print(f'{n}+{n1} = {s}')

    elif escolha == 2:
        s = n - n1
        print(f'{n}-{n1}={s}')

    elif escolha == 3:
        s = n * n1
        print(f'{n}+{n1}={s}')

    elif escolha == 4:
        s = n / n1
        if n1 == 0:
            print('nao se divide por 0')
            continue

    

    
    

