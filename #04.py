primeiro = int (input('Digite o primeiro valor'))
segundo = int (input('Digite o segundo valor'))
if primeiro > segundo:
    print(f' o primeiro numero digitado que foi {primeiro} é maior que o segundo numero digitado que foi {segundo}')

elif primeiro == segundo:
    print('Os dois numeros sao iguais')

else:
    print (f'o segundo numero digitado que foi {segundo} é maior que o primeiro numero digitado que foi {primeiro}')