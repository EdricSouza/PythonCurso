#jogador
desafio = 'Desafio 93'
print(f'{desafio:=^50}')

jogador = dict()
gol = []
total = 0

jogador['Nome'] = str(input('Digite o nome do jogador: '))
q = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

for cont in range(0, q):
    g = (int(input(f'Digite quantos gols ele fez no {cont + 1}° jogo: ')))
    gol.append(g)
    jogador['gol'] = gol.copy()
    total += g
    jogador['total'] = total

print('=-='*20)

for k,v in jogador.items():
    print(f'O campo {k} tem como valor: {v}')

print('=-='*20)

print(f'O jogador {jogador['Nome']} jogou ')

for v in jogador['gol']:
    part = 1
    print(f'Na {part}° partida, fez {v} gols')
    part += 1