print ('LOJAS FAUCZ')
preço = float (input('preço das compras'))
print(''' FORMAS DE PAGAMENTO
[1] A VISTA DINHEIRO/PIX 
[2] A VISTA CARTAO
[3] 2X CARTAO
[4] 3X OU MAIS NO CARTAO''')

opçao = int (input('Digite a opçao desejada de pagamento'))

if opçao == 1:
    novo = preço - (preço * 10 / 100)
    print(f'Sua opçao foi a vista dinheiro/pix, com isso voce tem desconto de 10% e o valor saira {novo}')

elif opçao == 2:
    novo = preço - (preço * 5 / 100)
    print(f'sua opçao foi a vista no cartao e com isso voce tera um desconto de 5% e saira {novo}')

elif opçao == 3:
    novo = preço
    parcela = novo / 2
    print(f'voce escolheu a opçao 2x no cartao e com isso nao temos desconto para voce e voce ira pagar no valor de {novo} e suas parcelas em 2x cada uma saira por {parcela}')

elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totpar = int (input('Digite em quantas parcelas voce deseja pagar'))
    parcela = total / totpar
    print(f'Voce escolheu a opçao de 3x ou mais no cartao, com isso sua compra terá um juros de 20% e com isso voce tera que pagar um valor total de {total}, em {totpar}x e saira cada parcela por {parcela}') 
