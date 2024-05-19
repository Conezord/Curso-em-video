#ler uma frase e dizer qts x aparece 'A', em que posição a primeira vez(L), em que posição a ultima vez(R)

frase = str(input('Digite uma frase: '))

vezesA = frase.count('a')
primeiroA = frase.find('a')
ultimoA = frase.rfind('a')


print('A letra a aparece {} vezes'.format(vezesA))
print('O primeiro a aparece na posição {}'.format(primeiroA))
print('O último a aparece na posição {}'.format(ultimoA))