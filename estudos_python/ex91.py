from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
jogada = []
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
jogada = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(jogada):
    print(f'Em {i+1}° lugar ficou o {v[0]} com {v[1]} pontos')
    sleep(1)
    