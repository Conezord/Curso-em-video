#calculando descontos

preço = float(input('Qual o preço do produto? '))
desconto = float(input('Qual a porcentagem do desconto? '))

print('O Preço é de R${} e com o desconto de {}% fica R${}'.format(preço, desconto, preço*((100-desconto)/100)))
