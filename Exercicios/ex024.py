#checar se a cidade COMEÇA com a palavra santo(independente de ter maiuscula, minuscula, espaço antes, etc)

cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip()

print(cidade[:5].upper() == 'SANTO')