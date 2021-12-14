n = s = 0
while n != 999:
    n = int(input('digite um valor (999 to stop) : '))
    if n == 999:
        break
    s += n
#print('a soma vale {}'.format(s))

print(f'a soma dos valores foi! {s}') # F STRINGS, f antes do print