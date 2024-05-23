nome= str (input('Qual seu nome ? '))
if nome == 'Miguel':
    print ('Nome lindo')

elif nome == 'Joao' or nome == 'Julio':
    print ('Nome feio')

elif nome in 'ana joaquim maria':
    print ('Maneiro')

else:
    print('Nome comum')

print('Tchau')