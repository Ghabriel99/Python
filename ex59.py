n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
   print('''  
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS
[5] EXIT''')
opcao = int(input('>>>>> Qual opção? '))
if opcao == 1:
    soma = n1+n2
    print('A soma entre {} e {} é {}'.format(n1,n2,soma))
elif opcao == 2:
    produto = n1*n2
    print('A multuplicacao entre {} e {} é {}'.format(n1,n2,produto))
elif opcao == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
        print('entre {} e {} o maior valor é '.format(n1,n2,maior))
elif opcao == 4:
    print('informe novamente: ')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))

elif opcao == 5:
    print('enddd')

else:
    print('try again')







