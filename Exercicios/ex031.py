#preço da passagem de acordo com a distancia da viagem

distancia = float(input('Qual a distância da sua viagem: '))
print('Sua viagem tem {}km de distância.'.format(distancia))
if distancia <= 200:
    print('Sua passagem vai custar R${:.2f}.'.format(distancia * 0.50))
else:
    print('Sua passagem vai custar R${:.2f}.'.format(distancia * 0.45))
