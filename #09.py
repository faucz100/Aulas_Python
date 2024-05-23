from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('''Suas opçoes:
[1]PEDRA
[2]PAPEL
[3]TESOURA''')
jogador = int (input('Digite sua opção'))
print(f'Computador jogou {itens[computador]} ')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')
    else:
        print('OPÇAO INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('Empatou')

    elif jogador == 2:
        print('jogador ganhou')

    else:
        print('OPÇAO INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('jogador ganhou')

    elif jogador == 1:
        print('computador ganhou')

    elif jogador == 2:
        print('EMPATOU')
    else:
        print('OPÇÃO INVALIDA')


