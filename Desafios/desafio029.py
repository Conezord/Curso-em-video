#ler a velocidade de um carro e se for acima de 80km/h
#multa de 7 reais por cada km acima do limite

velocidade = int(input('Qual a velocidade do carro em km/h? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado. Pague a multa de R${}'.format(multa))
else:
    print('Siga em frente')