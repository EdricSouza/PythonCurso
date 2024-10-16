#analise
desafio = 'Desafio 75'
print(f'{desafio:=^50}')

numero = (
            int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite outro número: ')),
        )

print(numero)

print(numero.count(9))
print(numero.index(3) + 1)
par = 0

for n in numero:
    if n % 2 == 0:
        par += 1

print(par)