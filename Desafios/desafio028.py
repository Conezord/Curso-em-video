#computador pensar em um numero de 0 a 5
#pedir ao usuario tentar adivinhar o numero escolhido
import random

numero = int(input('Tente adivinhar o número escolhido de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(lista)
print('Você escolheu o número {}'.format(numero))
print('A máquina escolheu o número {}'.format(aleatorio))

if numero == aleatorio:
    print('Você acertou!')
else:
    print('Você perdeu!')