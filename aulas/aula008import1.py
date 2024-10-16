from math import sqrt, ceil, floor

#pacotes (import)

aula = 'Aula 08'
print(f'{aula:=^50}')

num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é arredondada {ceil(raiz   )} pra cima e {floor(raiz)} pra baixo') 