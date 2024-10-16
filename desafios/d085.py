#par e impar
desafio = 'Desafio 85'
print(f'{desafio:=^50}')

numeros = [[], []]
t = 1
while True:
    numero = int(input(f'Digite o {t}° número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

    t += 1
    if t == 8:
        break

print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')