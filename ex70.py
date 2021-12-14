total = 0

while True:
    p = str(input('Nome do produto: '))
    preco = float(input('Preço: RS '))
    total += preco

    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'Nn':
      break

print('THE END')
print(f'O total da compra foi {total}')