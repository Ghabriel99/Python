distancia = float(input('digite a distancia da viagem: '))
print('voce vai viajar {} km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O PREÇO DA PASSAGEM É {} REAIS'.format(preco))