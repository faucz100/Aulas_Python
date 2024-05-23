n= 0
cont = 0
soma = 0
n = int (input('DIGITE O VALOR'))
while n != 999:
    
    soma += n
    cont += 1
    n = int (input('DIGITE O VALOR')) 
    
print(f'voce digitou {cont} numero e a soma deles foi {soma}')
    
