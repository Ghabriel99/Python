print('RESOLVENDO A PA')

p = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        cont +=1
        termo += r
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Foram mostrados {} termos ao total.'.format(total))
