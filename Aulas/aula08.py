# Módulos

# import + biblioteca = traz tudo
# from + biblioteca + importa + item especifico = traz somente
# uma parte da biblioteca
# exemplo: import math = traz tudo / from math import sqrt = traz só raiz quadrada

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

