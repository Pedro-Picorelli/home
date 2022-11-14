pessoas = []
pessoa = {}
idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'FM':
        print('Erro! Por favor apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while cont not in 'SN':
        print('Erro! Por favor apenas S ou N')
        cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'-='*30)
print(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {idade / len(pessoas)} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for i in pessoas:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['idade'] > (idade / len(pessoas)):
        print(f'nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')