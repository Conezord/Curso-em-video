#condições simples e compostas pt1
#condição simples tem apenas um IF
#condição composta tem um IF e um ELSE, exemplo:

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é {}'.format(m))
if m >= 6.0:
    print('Parabéns, você passou de ano')
else:
    print('Que pena, você não passou. Estude mais')