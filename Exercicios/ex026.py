# ler uma frase e quantas vezes aparece a letra A, primeira e ultima vez que aparece

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A')+1))