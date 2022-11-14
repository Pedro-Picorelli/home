from operator import index


pessoa = []
lista = []
mai = men = 0
while True:
   pessoa.append(str(input('Informe o nome: ')))
   pessoa.append(float(input("Informe o peso:")))
   if len(lista) == 0:
       mai = men = pessoa[1]
   else:
       if mai < pessoa[1]:
            mai = pessoa[1]
       if men > pessoa[1]:
            men = pessoa[1]
   lista.append(pessoa[:])
   pessoa.clear()
   
   x = str(input('Quer continuar? [N/S]: ')).upper().strip()
   if x[0] in 'N':
       break
    #    x = input('[Opção invalida]: Quer continuar? [N/S]: ').upper().strip()

print(f'Cadstros: {len(lista)}')
print(f'O maior peso foi {mai} ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso foi {men} ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}, ', end='')