desafio = 'Desafio 63'
print(f'{desafio:=^50}')

frase = 'Fibonacci'
print(f'{frase:=^50}')

q = int(input('Quantos números da sequência você quer que apareça? '))
a = 0

while a < q:
    q = (q-1) + (q-2)
    print(q)
    a += 1