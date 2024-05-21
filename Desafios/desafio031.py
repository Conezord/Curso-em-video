# calcular o preço da passagem de onibus cobrando:
# 50 centavos se a viagem for até (maior ou igual) 200km
# 45 centavos se a viagem for mais de (maior que) 200km

distancia = float(input('Quantos km tem a viagem inteira? '))
tarifa1 = distancia * 0.50
tarifa2 = distancia * 0.45

if distancia <= 200:
    print('A passagem custa {:.2f}'.format(tarifa1))
else:
    print('A passagem custa {}'.format(tarifa2))