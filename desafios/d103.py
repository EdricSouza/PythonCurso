#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg('Jogador')

def camp(nome='<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

jogador = input('Nome do jogador: ')
gol = input('Números de gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    camp(gols=gol)
else:
    camp(jogador, gol)