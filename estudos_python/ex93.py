jogador = {}
lista = []
jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(jogos):
    gols = int(input(f' Quantos gols na partida {i}? '))
    lista.append(gols)
jogador['gols'] = lista[:]
jogador['total'] = sum(lista)

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f' {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')