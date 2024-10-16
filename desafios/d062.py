#PA
desafio = 'Desafio 62'
print(f'{desafio:=^50}')

frase = 'Pogressão aritmética'
print(f'{frase:=^50}')

n = int(input('Digite o valor inicial: '))
r = int(input('Qual é a razão: '))

a = 0
while a < 10:
    if a == 0:
        print(f'\u001b[32m{n} \u001b[0m\u001b[31m->\u001b[0m', end='')
    elif a == 9:
        print(f'\u001b[32m {n} \u001b[0m')
    elif a != 10:
        print(f'\u001b[32m {n} \u001b[0m\u001b[31m->\u001b[0m', end='')
    n += r
    a += 1

m = 1
a = 0
while m != 0:
    m = int(input('\nQuantos termos você quer mostrar a mais: '))
    a = 0
    while a < m:
        if a == 9:
            print(f'\u001b[32m {n} \u001b[0m')
        elif a != 10:
            print(f'\u001b[32m {n} \u001b[0m\u001b[31m->\u001b[0m', end='')
        n += r
        a += 1

