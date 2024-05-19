# verificar se tem silva dentro do nome da pessoa

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))