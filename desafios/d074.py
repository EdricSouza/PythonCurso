from random import randint

#maior e menor
desafio = 'Desafio 74'
print(f'{desafio:=^50}')

n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)

print(n)

menor = 11
maior = 0
c = 0

for c in n:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')