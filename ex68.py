from random import randint
v = 0
while True:
    j = int(input('Diga um valor: '))
    c = randint(0,11)
    total = j + c
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('PAR OU IMPAR? ')).strip().upper()
    print(f'Voce jogou {j} e o computador {c}. Total de {total}, ', end='')
    print('DEU PAR'if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'Pp':
        if total % 2 == 0:
            print('YOU WIN')
            v += 1
        else:
          print('YOU LOOSE')
          break
    elif tipo == 'Ii':
       if 2 != 1:
           print('YOU LOOSE')
           break
       else:
           print('YOU WIN')
           v += 1
print(f'GAME OVER! Voce ganhou {v} vezes')

