while True:
    sexo = str (input('Digite seu sexo [M]/[F]'))
    if sexo not in 'MmFf':
        print('Voce ditou errado, por favor digite novamente')
    else:
        break


print('ok')