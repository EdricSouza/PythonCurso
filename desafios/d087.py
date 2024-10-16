#Matriz +
desafio = 'Desafio 87'
print(f'{desafio:=^50}')

matriz = [[], [], []]
somapar = 0
soma3 = 0
maior = 0

for t in range(0,3):
    for c in range(0,3):
        matriz[t].append(int(input(f'Digite o número na posição [{t+1},{c+1}]: ')))

print('-='*30)

for i in range (0,3):
    for c in range (0,3):
        print(f'[ {matriz[i][c]} ]', end='')
    print('')

for i in range (0,3):
    for c in range (0,3):
        if matriz[i][c] % 2 == 0:
            somapar += matriz[i][c]

for d in range(0,3):
    soma3 += matriz[d][2]

for d in range(0,3):
    if matriz[1][d] > maior:
        maior = matriz[1][d]

print(f'A soma dos pares é: {somapar}')
print(f'A da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior}')