#Caixa
desafio = 'Desafio 71'
print(f'{desafio:=^50}')

valor = int(input('Qual valor você quer sacar? '))
c50 = 0
c20 = 0
c10 = 0
c1 = 0

while True:
    if valor >= 50:
        c50 += 1
        valor -= 50
    elif valor >= 20:
        c20 += 1
        valor -= 20
    elif valor >= 10:
        c10 += 1
        valor -= 10
    elif valor >= 1:
        c1 += 1
        valor -= 1
    else:
        break

if c50 > 1:
    print(f'São {c50} cédulas de 50')
if c20 > 1:
    print(f'São {c20} cédulas de 20')
if c10 > 1:
    print(f'São {c10} cédulas de 10')
if c1 > 1:
    print(f'São {c1} cédulas de 1')