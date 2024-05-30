# ler peso e altura, calcular imc e mostrar status de acordo com a tabela

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em CM: '))
imc = (peso / ((altura/100) **2))
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif 40 <= imc:
    print('Obesidade mórbida')
