#muyltiplos de 3
desafio = 'desafio 47'
print(f'{desafio:=^50}')

for c in range(0,500):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c)