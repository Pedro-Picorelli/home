jogadores = []
jogador = {}
lista = []
while True:
    jogador.clear()
    lista.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(jogos):
        gols = int(input(f' Quantos gols na partida {i}? '))
        lista.append(gols)
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    jogadores.append(jogador.copy())
    while True:
        x = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if x not in 'SN':
            print('ERRO!')
        else:
            break
    if x == 'N':
        break

print('-='*30)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"Total":<5}')
print('-'*60)

for k, v in enumerate(jogadores):
    print(f"{k:<4} {v['nome']:<15} {(v['gols'])} {v['total']:<5}")
quantidade = len(jogadores)
while True:
    while True:
        q = int(input('Qual jogador? (999 para parar) '))
        if q < 0 or q > quantidade and q != 999:
            print('Erro!')
        else:
            break
    if q == 999:
        break
    else:
        for i, v in enumerate(jogadores):
            if i == q:
                print(f"O jogador {v['nome']}")
                for i, v in enumerate(v['gols']):
                    print(f'No joga {i+1} fez {v} gols')