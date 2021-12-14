soma = cont = 0

while True:
    num = int(input('Digite um valor: (999 to stop): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi {soma}!')
