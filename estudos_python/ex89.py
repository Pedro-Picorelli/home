from operator import index


aluno = []
pessoa = []
while True:
    x = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    pessoa.append([x,n1,n2])
    
    c = str(input('Quer continuar? [S/N]')).strip().upper()
    if c[0] in 'N':
        break
print(f"{'No.':<4}{'Nome':<15}{'Media':<5}")
print('-'*25)
for i in range(len(pessoa)):
    print(f'{i:<4}{pessoa[i][0]:<15}{((pessoa[i][1]+pessoa[i][2])/2):<5}')
while True:
    n = int(input('Mostrar nota de qual aluno? (999 para parar):'))
    if n == 999:
        break
    elif n < len(pessoa):
        print(f'Notas de {pessoa[n][0]} são {pessoa[n][1],pessoa[n][2]}')
    else:
        print('OPÇÃO INVALIDA')
print('Fim')