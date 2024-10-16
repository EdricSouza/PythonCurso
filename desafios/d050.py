#pares
desafio = 'desafio 50'
print(f'{desafio:=^50}')

soma = 0
for c in range(0,7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma = soma + numero

print(f'A soma de todos os valores pares é: {soma}')