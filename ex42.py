r1 = float(input('Primeiro angulo: '))
r2 = float(input('Segundo angulo: '))
r3 = float(input('Terceiro angulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triangulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('nono')