medida = int(input('Digite quantos metros você deseja converter: '))
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print('Sua medida de {:.2f} metros convertida é'.format(medida))
print('{:.3f} km'.format(km))
print('{:.0f} cm'.format(cm))