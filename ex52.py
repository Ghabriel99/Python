
frase = str(input('Digite uma frase: ')).strip().upper()
plv = frase.split()
junto = ''.join(plv)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} É {} '.format(junto,inverso))
if inverso == junto:
    print('pre')
