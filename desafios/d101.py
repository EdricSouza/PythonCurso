from datetime import datetime

#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg('Votação')

def voto(anonasc):
    idade = datetime.today().year - anonasc
    if idade < 16:
        return 'negado'
    elif 16 >= idade < 18:
        return 'opcional'
    else:
        return 'obrigatório'

ano = int(input('Digite o ano em que nasceu: '))
opc = voto(ano)
print(f'Seu voto é {opc}')