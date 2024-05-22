#Jogo da Adivinhação 
from time import sleep
from random import randint

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer')
else:
    print('Ganhei! Pensei no número {} e não no {}'.format(computador, jogador))

