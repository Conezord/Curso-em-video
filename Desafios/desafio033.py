#ler 3 numeros e me dizer o maior e o menor

numero1 = int(input('Qual o primeiro número? '))
numero2 = int(input('Qual o segundo número? '))
numero3 = int(input('Qual o terceiro número? '))

lista = [numero1, numero2, numero3]
ordenada = sorted(lista)

print(ordenada)

print('o menor número é o {}'.format(ordenada[0]))
print('O maior número é {}'.format(ordenada[(len(lista)-1)]))
