#ordem de apresentação de 4 alunos

from random import shuffle

a1 = str(input('O primeiro aluno é: '))
a2 = str(input('O segundo aluno é: '))
a3 = str(input('O terceiro aluno é: '))
a4 = str(input('O quarto aluno é: '))
lista_alunos = [a1, a2, a3, a4]
shuffle(lista_alunos)

print('A ordem de apresentação é: ')
print(lista_alunos)