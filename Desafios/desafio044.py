#preço do produto considerando o metodo de pagamento

preco = float(input('Qual o preço do produto? R$'))
pgto = str(input('Qual o método de pagamento? ')).upper()

if pgto == "DINHEIRO" or "CHEQUE":
    print('O valor do produto ficou R${:.2f}'.format(preco * 0.9))
elif pgto == "CARTÃO" or "CARTAO":
    print('O valor do produto ficou R${:.2f}'.format(preco * 0.95))
elif pgto == "2x no cartão":
    print("o preço final é de R${}.".format(preco))
elif pgto == "3x ou mais":
    print('O preço final é de R${}'.format(preco * 1.2))