#ler o ano de nascimento e informe de acordo com a idade se:
# 1 - ainda vai se alistar
# 2 - é hora de alistar
# 3 - se já passou do tempo do alistamento
import datetime

nasceu = int(input('Qual o ano de nascimento? '))
hoje = datetime.datetime.today().year
idade_atual = hoje - nasceu
print('Você faz {} anos nesse ano'.format(idade_atual))
if idade_atual < 18:
    print('Não é a hora para você se alistar ainda')
    print('Você deverá se alistar daqui {} ano(s)'.format(nasceu - hoje + 18))
    saldo = 18 - idade_atual
    ano = hoje + saldo
    print('Seu ano de alistamento será em {}'.format(ano))
elif idade_atual == 18:
    print('É a hora de se alistar!')
elif idade_atual > 18:
    print('Já passou o tempo do alistamento')
    print('Você deveria ter se alistado {} ano(s) atrás'.format(hoje - nasceu - 18))
    saldo = idade_atual - 18
    ano = hoje - saldo
    print('Seu alistamento foi em {}'.format(ano))