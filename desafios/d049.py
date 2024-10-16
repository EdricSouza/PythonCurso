#tabuada
desafio = 'desafio 49'
print(f'{desafio:=^50}')

numero = int(input('Digite um valor: '))
print('\n')

for c in range (0,11):
    print(f'{numero} * {c} = {numero * c}')