#tabuada
desafio = 'Desafio 67'
print(f'{desafio:=^50}')

while True:
    n = int(input('Qual tabuada você quer ver? '))
    a = 0
    if n < 0:
        break
    while a <= 10:
        print(f'{n} * {a} = {n*a}')
        a += 1