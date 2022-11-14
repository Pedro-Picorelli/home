aluno = {'nome': str(input('Nome: ')),'media': float(input('Media: '))}
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
    
for k,v in aluno.items():
    print(f'- {k} é igual {v}')