primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão?:'))
decimo = primeiro + (12-1) * razao
for c in range (primeiro,decimo+razao,razao):
    print('{} '.format(c), end=' > ')
print('end')