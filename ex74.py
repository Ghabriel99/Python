from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')

for n in numero:
    print(f'{n}', end='')

print(f'\nThe higher value is {max(numero)}')
print(f'The lowest value is {min(numero)}')