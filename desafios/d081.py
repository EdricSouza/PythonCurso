#extraindo valores
desafio = 'Desafio 81'
print(f'{desafio:=^50}')

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    brk = input('Deseja continuar? ').capitalize().strip()
    if brk[0] == 'N':
        break

numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é: {numeros}')
print(f'Posui {len(numeros)} elementos')
if 5 in numeros:
    print(f'O números 5 se encontra na lista')
else:
    print(f'O números 5 não se encontra na lista')