#ler 3 lados de um triangulo e dizer se pode ou nao formar um triangulo

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

cond1 = (r1 + r2) > r3
cond2 = (r1 + r3) > r2
cond3 = (r2 + r3) > r1


if cond1 == True and cond2 == True and cond3 == True:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')