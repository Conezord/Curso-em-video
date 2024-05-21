#perguntar o salario e calcular o aumento
#para salarios maiores que 1250, aumenta 10%
#para salarios menores ou iguais a 1250, aumenta 15%

salario = float(input('Digite o seu salário: '))

if salario < 1250:
    print('Seu novo salário é de R${:.2f}'.format(salario * 1.15))
else:
    print('Seu novo salário é de R${:.2f}'.format(salario * 1.1))