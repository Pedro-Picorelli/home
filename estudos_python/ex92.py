from datetime import datetime
trabalhador = {}

atual = datetime.now().year
#35 anos de colaboração
trabalhador['nome'] = str(input('Nome: '))

ano = int(input('Ano de Nascimento: '))
trabalhador['idade'] = atual - ano

trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] - ano) + 35
    
print('-='*30)

for k, v in trabalhador.items():
    print(f' {k} tem o valor {v}')