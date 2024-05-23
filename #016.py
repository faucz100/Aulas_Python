maior = 0
menor = 0

for c in range(1,6):
    peso = float (input(f'Digite seu {c} peso'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'o maior peso foi {maior}kg e o menor foi {menor}kg')
