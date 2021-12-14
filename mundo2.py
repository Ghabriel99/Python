casa = float(input("Quanto quer pagar na casa: R$"))
salario = float(input('Quanto voce ganha: R$'))
anos = int(input("Em quantos anos voce vai pagar: "))
parcela= casa/(anos*12)
minimo= salario* 30/100

print('para pagar uma casa de {}R$, em {} anos '.format(casa, anos), end='')
print(' a parcela sera de {:3f} R$'.format(parcela))

if parcela <= minimo:
    print('ok')
else:
    print('negado')




