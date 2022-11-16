def text(tx):
    quant = len(tx) + 4
    print('-'*quant)
    print(f'  {tx}')
    print('-'*quant)

t = str(input('Informe o texto: '))
text(t)