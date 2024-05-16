# ordem do sorteio dos 4 alunos

import random

# alunos = ['João', 'Fernando', 'Gustavo', 'Lucas']
# random.shuffle(alunos)
# print(alunos)

# OU

alunos = ['João', 'Fernando', 'Gustavo', 'Lucas']
ordem = random.sample(alunos, k=4)
print(ordem)
