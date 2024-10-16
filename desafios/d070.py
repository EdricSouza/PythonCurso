#produtos
desafio = 'Desafio 70'
print(f'{desafio:=^50}')

mpreco = 0
mil = 0
total = 0
c = 0
nm = ""

while True:
    nome = input('Digite o nome do produto: ').capitalize().strip()
    preco = float(input('Digite o preço dele: '))

    total += preco
    if preco >= 1000:
        mil += 1
    if c == 0:
        mpreco = preco
        nm = nome
    elif preco < mpreco:
        mpreco = preco
        nm = nome
    c += 1

    t = input('Deseja continuar? ').capitalize().strip()
    if t[0] == 'N':
        print('_________________________________')
        break

print(f'O valor total é de R${total}')
print(f'{mil} produtos, são acima do valor de 1000 reais')
print(f'O produto mais barato é: {nm} de R${mpreco}')
