sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor informe novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))