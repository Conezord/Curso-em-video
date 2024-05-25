# analisando triangulo

reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))
if (reta1 + reta2) >= reta3 and (reta1 + reta3) >= reta2 and (reta2 + reta3) >= reta1:
    print('Com essas retas, você CONSEGUE formar um triângulo')
else:
    print('NÃO é possivel formar um triângulo com essas 3 retas')

'''também é possivel resolver esse exercicio usando a regras
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
'''