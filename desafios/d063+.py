desafio = 'Desafio 63'
print(f'{desafio:=^50}')

frase = 'Fibonacci'
print(f'{frase:=^50}')

q = int(input('Quantos números da sequência você quer que apareça? '))
a = 3
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')

while a <= q:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    a += 1
print(' - fim')