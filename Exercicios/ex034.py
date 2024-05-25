# salário do funcionario e aumento em %

salario = float(input('Digite o salário aqui: R$'))
if salario <= 1250:
    novo = salario * 1.15
else:
    novo = salario * 1.10
print('Seu salário recalculado será de R${:.2f}'.format(novo))