# par ou impar

numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
print('O resultado foi {}.'.format(resultado))