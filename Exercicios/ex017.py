# tem 2 formas de fazer isso, metodo matemático e com a biblioteca math
# forma 1
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa mede {:.2f}'.format(hi))'''

#forma 2

import math
co = float(input('Comprimento do cateto oposto é: '))
ca = float(input('Comprimento do cateto adjacente é: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}.'.format(hi))