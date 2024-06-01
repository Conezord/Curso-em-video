#categoria de natação de acordo com a idade
import datetime
nascimento = int(input('Qual o ano de nascimento do atleta? '))
data = datetime.datetime.today().year
ano = data - nascimento

if ano <= 9:
    print('Categoria MIRIM')
elif 9 < ano <= 14:
    print('Categoria INFANTIL')
elif 14 < ano <= 19:
    print('Categoria JUNIOR')
elif 19 < ano <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')