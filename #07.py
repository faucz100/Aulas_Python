from datetime import date
atual = date.today().year

nasc = int (input('Digite seu ano de nascimento'))
idade = atual - nasc

if idade <= 9:
    print(f'Voce nasceu em {nasc}, tem {idade} e está na categoria mirim')

elif idade > 9 and idade <=14:
    print('classificação infantil')

elif idade > 14 and idade <= 19:
    print('classificação junior')

elif idade > 19 and idade <= 25:
    print('classificação senior')

else:
    print('Classificação master')