#ler o nome de uma cidade e dizer se começa ou nao com o nome 'SANTO'

cidade = str(input('Digite o nome da sua cidade: '))

check = 'SANTO' in cidade

print(check)

"""aqui está errado, ele nao checa tudo
apenas checa se exatamente a palavra SANTO está na string
mas devemos checar todos os tipos ex Santos SaNtoS, etc.
jogamos tudo pra maiuscula e checamos se é igual a SANTO
resolução no arquivo ex024.py"""
