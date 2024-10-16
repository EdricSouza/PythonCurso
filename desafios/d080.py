#valor
desafio = 'Desafio 80'
print(f'{desafio:=^50}')

numero = []
c = 0

for c in range(0,5):
    n  = int(input('Digite um número: '))
    if c == 0 or c > numero[- 1]:
        numero.append(n)
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos, n)
                break
            pos += 1

print(f'Os valores printados em ordem foram: {numero}')