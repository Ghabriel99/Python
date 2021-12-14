resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print("voce digitou {} numeros e a media foi {} ".format(quant, num))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))