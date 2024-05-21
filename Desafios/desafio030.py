#leia um numero e diga se é par ou impar
import math

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero)) 