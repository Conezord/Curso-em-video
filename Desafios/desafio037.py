#ler um número e escolher a base de conversão 1, 2 ou 3

numero = int(input('Digite o número que quer converter: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente')
