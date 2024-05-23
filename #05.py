from datetime import date
atual = date.today().year
nasc = int (input('Digite o ano que voce nasceu'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce esta na idade certa para se alistar, procure uma junta militar para alistamento')

elif idade > 18:
    falta = idade - 18
    print(f'Voce deveria ter se alistado há {falta} anos, vá se alistar ')

elif idade < 18:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para voce se alistar')