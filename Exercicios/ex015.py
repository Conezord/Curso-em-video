# Aluguel de carros

dias = int(input('Por quantos dias foi alugado? '))
km = float(input('Quantos km rodados? '))

print('O total a pagar é R${:.2f}.'.format((dias * 60) + (km * 0.15)))