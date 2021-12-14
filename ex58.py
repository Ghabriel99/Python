from random import randint
computer = randint(0, 10)
print("I am your computer... I have thought a number between 0 and 10.")
print("Can you guess?")
acertou = False
shots = 0
while not acertou:
    jogador = int(input('Say a number: '))
    shots += 1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('+')
        elif jogador > computer:
            print('-')

print('Right with {} shots'.format(shots))