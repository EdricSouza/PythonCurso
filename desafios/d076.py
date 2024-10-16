#Preços
desafio = 'Desafio 76'
print(f'{desafio:=^50}')

lista = (
            'Lapis', 1.7,
            'Caneta', 3,
            'Régua', 5.7,
            'Caneta 4 cores', 7.7,
            'Corretivo', 10.7
        )

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')