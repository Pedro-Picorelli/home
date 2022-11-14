valores = [[0,0,0],[0,0,0],[0,0,0]]
ter = par = mai = 0
for l in range(3):
    for c in range(3):
        x = int(input(f"Digite um valor: [{l},{c}] "))
        valores[l][c] = x
        if c == 2:
            ter += x
        if x%2 == 0:
            par+=x
        if l == 1:
            if mai < x:
                mai = x            
for l in range(3):
    for c in range(3):
        print(f'[{valores[l][c]:^5}]', end='')
    print()  
print(f'pares soma {par}')
print(f'soma terceira colunba {ter}')
print(f'maior segunda linha {mai}')