# Ler um numero de 0 a 9999 e printar na tela cada um separadamente

num = str(input('Digite um número de 0 a 9999: '))

len(num)

print('unidade:', num[3])
print('dezena:', num[2])
print('centena:', num[1])
print('milhar:', num[0])

#nao sei corrigir o erro quando tem menos de 4 numeros