from cgi import print_form


valores = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(3):
    for c in range(3):
        valores[l][c] = int(input(f"Digite um valor [{l,c}] "))

for l in range(3):
    for c in range(3):
        print(f'[{valores[l][c]:^5}]', end='')
    print()