# ler um nome completo e puxar o primeiro e ultimo nome 

n = str(input('Digite seu nome completo: ')).strip()
name = n.split()

print(name)
print('É um prazer te conhecer')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[len(name)-1]))
