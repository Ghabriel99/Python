money= float(input('digite um valor RS :'))
if money <=1250:
    novo = money + (money * 15/100)

else:
    novo= money + (money * 10/100)
print('quem ganhava RS{} passa a ganhar {} agora'.format(money,novo))

