soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
      cont += c
      soma += 1
print(' a soma de todos valores é {}'.format(soma))
print('o numero de divisiveis foi {}'.format(cont))
