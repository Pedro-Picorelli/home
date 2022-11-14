import imp


numeros = [[],[]]

for n in range(7):
    x = int(input("Digite um numero: "))
    if (x % 2) == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
numeros[0].sort()
numeros[1].sort()
print(f'pares {numeros[0]}')
print(f'impares {numeros[1]}')