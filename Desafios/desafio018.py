# leia um angulo e mostre o sen, cos e tg

import math
angulo = float(input('Qual o valor do ângulo? '))
cosseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)

print('Cosseno do angulo {} é {}, seno {} e tangente {}'.format(angulo, cosseno, seno, tangente))
