num = int (input('Digite um numero inteiro '))
print('''ESCOLHA UM NUMERO PARA SUA CONVERSÃO:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
opção = int (input('Digite sua opçao desejada '))
if opção == 1:
    print(f'{num} convertido para binario é = {bin(num)[2:]}')

elif opção == 2:
    print(f'o {num} convertido para octal é {oct(num)[2:]}')

elif opção == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')

else:
    print('opção invalida')

    