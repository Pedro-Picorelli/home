from random import randint
from time import sleep
# from turtle import clear
j = int(input('Quantos jogos? '))
lista = []
for i in range(j):
    for c in range(6):
        x = randint(1,60)
        if x not in lista:
            lista.append(x)
    print(f'Jogo {i+1}° {lista}')
    lista.clear()
    sleep(1)