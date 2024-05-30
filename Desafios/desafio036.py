#emprestimo bancario

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Pretende pagar em quantos anos?'))
meses = anos * 12
prestacao = casa / meses

if prestacao <= (salario * 0.3):
    print('Empréstimo \033[32mAPROVADO\033[m')
    print('O valor da prestação é R${:.2f} mensal'.format(prestacao))
elif prestacao > (salario * 0.3):
    print('Empréstimo \033[31mNEGADO\033[m')