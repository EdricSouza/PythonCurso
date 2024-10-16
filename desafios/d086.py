#Matriz
desafio = 'Desafio 84'
print(f'{desafio:=^50}')

matriz = [[], [], []]

for t in range(0,3):
    for c in range(0,3):
        matriz[t].append(int(input(f'Digite o número na posição [{t+1},{c+1}]: ')))

print('-='*30)

for i in range (0,3):
    for c in range (0,3):
        print(f'[ {matriz[i][c]} ]', end='')
    print('')