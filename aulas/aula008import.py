import math
import random

#pacotes (import)

aula = 'Aula 08'
print(f'{aula:=^50}')

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é arredondada {math.ceil(raiz   )} pra cima e {math.floor(raiz)} pra baixo') 

print(random.random())
print(random.randint(1,100))