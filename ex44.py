print('{:=^30}' . format('FRIEDDDS STORE'))
preco = float(input('PREÇO TOTAL DAS COMPRAS RS: '))
print('''
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x cartão
[4] 3x ou mais
''')
opcao=int(input('Qual é a opção: '))
if opcao == 1:
    total= preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total =  preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de RS{} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(' Sua compra será parcelada em {}x de RS{:.2f} com 20% de juros totais'.format(totalparc,parcela))
else:
    total = 0
    print('OPCAO INVÁLIDA')
print('Sua compra de RS{:.2f} vai custar RS{:.2f} no final '.format(preco, total))







