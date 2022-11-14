from random import randint
estudar = ['python', 'js', 'html e css', 'calculo','em aberto']
dias = ['seg', 'ter', 'quar', 'quint', 'sex']
sorteio = []
i = 0
c = 0
while i < 5:
    x = randint(0,4)
    if x not in sorteio:
        sorteio.append(x)
        print(f'Na {dias[c]}, vou estudar {estudar[x]}')
        c+=1
        i +=1
    else:
        i -= 1
    