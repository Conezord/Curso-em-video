#triangulo com 2 retas E tipo de triangulo

r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))
tipo = "Equilátero" if r1 == r2 == r3 else "Isóceles" if r1 == r2 or r1 == r3 or r2 == r3 else "Escaleno"


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo com essas retas')
    #poderia colocar um if aqui, dentro do if printando os tipos de triangulos
    print('Esse é um triângulo {}'.format(tipo))
else:
    print('Não é possível formar um triângulo com essas retas')