somaid = 0
media = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0

for c in range (1,5):
    print(f'{c} pessoa')
    nome = str (input(' nome '))
    idade = int (input(' idade '))
    sexo = str (input(' sexo [M]/[F] ')).strip()
    somaid += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1




media= somaid / 4
print(f'a media de idade do grupo é {media}')
print(f'O homem mais velho é {nomemaisvelho} e tem {maioridadehomem} anos')
print(f'ao todo sao {totmulher20} mulher com menos de 20 anos')

