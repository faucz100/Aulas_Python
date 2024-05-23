s= 0
cont = 0
for c in range (1,501,2):
    if c %3:
        s += c
        cont += 1
print(f'a soma dos {cont} numeros da o valor de {s}') 