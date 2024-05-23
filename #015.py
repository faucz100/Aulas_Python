from datetime import date
atual = date.today().year
maior=0
menor=0

for c in range (1,8):
    nasc = int (input(f'em que ano a {c} pessoa nasceu?'))
    idade = atual - nasc

    if idade >= 18:
        maior += 1
        
    else:
        menor += 1
print(f'ao todo tivemos {menor} pessoas menor de idade e {maior} pessoas maior de idade')
