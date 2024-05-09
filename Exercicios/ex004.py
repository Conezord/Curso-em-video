#igual ao desafio 4, porem com mais informações
#trazendo uma pergunta antes de cada verificação

coisa = input('Digite qualquer coisa: ')

print('O tipo primitivo de', coisa, 'é:', type(coisa))
print(coisa, 'é alfanumerico? ', coisa.isalpha())
print(coisa, 'é um número? ', coisa.isnumeric())