tupla = ('Pneu', 2.0,
         'Aro', 29,
         'Cubo', 7),
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}')
    else:
        print(f'RS{tupla[pos]}')
