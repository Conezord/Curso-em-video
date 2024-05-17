#sorteio de 1 aluno entre 4
#metodo CHOICE da classe RANDOM
import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista_alunos = [n1, n2, n3, n4]

escolhido = random.choice(lista_alunos)
print('O aluno escolhido foi {}'.format(escolhido))