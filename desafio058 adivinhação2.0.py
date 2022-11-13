from time import sleep
from random import randint
pc = randint(0, 10)
sleep(1)
print('Olá!')
sleep(1.5)
print('Sou seu computador...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
sleep(2)
acertou = False
cont = 0
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    cont += 1
    if palpite == pc:
        acertou = True
    else:
        if palpite < pc:
            print('Mais ... Tente mais uma vez.')
        elif palpite > pc:
            print('Menos ... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas')