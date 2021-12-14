tupla = ('zero', 'um', 'dois', 'tres')
while True:
       n = int(input('Digite um numero entre 0 e 20: '))
       if 0 <= n <= 20:
           break
       print('TRY AGAIN', end=' ')
print(f'Voce digitou o numero {tupla[n]}')