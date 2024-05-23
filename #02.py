valorcasa = float (input('Qual valor da casa que deseja comprar? R$'))
salario = float (input('Digite seu salario'))
anos = int (input('quantos anos vc irá querer fazer o financiamento?'))
prestação = valorcasa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa {valorcasa:.2f} em {anos} anos')
print(f'a prestação sairá {prestação:.2f}')

if prestação <= minimo:
    print('emprestimo concedido')

else:
    print('nao concedido')