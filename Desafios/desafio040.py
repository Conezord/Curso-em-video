#ler duas notas e mostrar a media, de acordo com a media mostrar se:
#1 reprovou - abaixo de 5
#2 recuperação - entre 5 e 6.9
#3 aprovado - acima de 7

nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO')
elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')