# ler dois numeros inteiros e compare eles, mostrando:
# 1- mostrar se o primeiro valor é o maior
# 2- segundo valor é maior 
# 3- sao iguais

num1 = int(input('Qual o primeiro número: '))
num2 = int(input('Qual o segundo número: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Os números são iguais')