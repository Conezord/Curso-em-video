#computador jogando jokenpo com vc
import time
import random

print('-=-' *20)
print(' ' * 20, 'JO KEN PO')
print('-=-' *20)
time.sleep(2)
jogador = str(input('Escolha Pedra, Papel ou Tesoura: '))
lista = ['Pedra', 'Papel', 'Tesoura']
maquina = random.choice(lista)

print('Hmmm... Estou pensando....')
time.sleep(2)
print('Eu escolhi {}'.format(maquina))

if jogador.upper() == 'PEDRA' and maquina == 'Pedra' or jogador.upper() == 'PAPEL' and maquina == 'Papel' or jogador.upper() == 'TESOURA' and maquina == 'Tesoura':
    print('Empate!')
elif jogador.upper() == 'PEDRA' and maquina == 'Papel' or jogador.upper() == 'PAPEL' and maquina == 'Tesoura' or jogador.upper() == 'TESOURA' and maquina == 'Pedra':
    print('Você Perdeu!')
elif jogador.upper() == 'PEDRA' and maquina == 'Tesoura' or jogador.upper() == 'PAPEL' and maquina == 'Pedra' or jogador.upper() == 'TESOURA' and maquina == 'Papel':
    print('Você Venceu!')