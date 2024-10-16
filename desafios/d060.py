#fatorial
desafio = 'Desafio 60'
print(f'{desafio:=^50}')

frase = 'Calculadora Fatorial'
print(f'{frase:=^50}')

numero = int(input('Digite o valor: '))
valor = numero

print(f'{numero}', end='')

while numero > 1:
    valor = valor * (numero - 1)
    if numero != 1:
        print(f' * {numero - 1}', end='')
    numero -= 1

print(f'= {valor}')