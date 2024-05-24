#puxar o menor e maior valor dentre 3 valores dados

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('O primeiro número digitado foi {}.'.format(n1))
print('O segundo foi {}.'.format(n2))
print('O terceiro foi {}.'.format(n3))
# verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor é {}'.format(menor))
print('o maior valor é {}.'.format(maior))
