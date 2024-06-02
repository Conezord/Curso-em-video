#preço do produto considerando o metodo de pagamento
print('=' * 20, 'LOJAS CONE', '='* 20)
preco = float(input('Qual o preço total das compras? R$ '))
pgto = int(input('''Qual o método de pagamento? 
[ 1 ] - à vista no dinheiro ou cheque
[ 2 ] - à vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais
Sua opção: '''))

if pgto == 1:
    print('O valor do produto ficou R${:.2f}'.format(preco * 0.9))
elif pgto == 2:
    print('O valor do produto ficou R${:.2f}'.format(preco * 0.95))
elif pgto == 3:
    print("o preço final é de R${}.".format(preco))
    print('Cada parcela ficou R${}'.format(preco/ 2))
elif pgto == 4:
    parcelas = (int(input('Qual o número de parcelas? ')))
    print('O preço final é de R${}'.format(preco * 1.2))
    print('Cada parcela ficou R${}'.format((preco * 1.2)/ parcelas))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')