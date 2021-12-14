peso = float(input('Seu peso atual: (Kg) '))
altura = float(input('Sua altura: (m)'))

imc = peso / (altura**2)
print(' O IMC dessa pessoa é de {:.1f} '.format(imc))

if imc <=18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc <=25:
    print('Voce esta no Peso ideal')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc <= 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE FODA')