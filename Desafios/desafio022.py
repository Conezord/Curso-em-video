# Nome completo de uma pessoa

name = str(input('Escreva seu nome completo: '))

print(name.upper())

print(name.lower())

lista = name.split()
print(len(''.join(lista)))

primeiro_nome = lista[0]
print(len(primeiro_nome))