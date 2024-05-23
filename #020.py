from random import randint
pc = randint (0,10)
palpites = 0
print('Acabei de pensar em um numero entre 0 e 10, voce consegue adivinhar qual foi ? ')
acertou = False
while not acertou:
    jogador = int (input('qual seu numero'))
    palpites +=1
    if jogador == pc:
        acertou= True
    else:
        if jogador < pc:
            print('Mais')

        elif jogador > pc:
            print('menos')
print(f'voce acertou com {palpites} palpites')
