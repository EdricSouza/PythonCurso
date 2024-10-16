import colorama

#primos
desafio = 'desafio 51'
print(f'{desafio:=^50}')

numero = int(input('Digite um número aqui: '))

cont = 0
for c in range(1,numero + 1):
    if numero % c == 0:
        print(f'\u001b[33m{c}', end=' ')
        cont += 1
    else:
        print(f'\u001b[35m{c}', end=' ')
        
if cont > 2:
    print(f'\n\u001b[0mEle não é primo pois foi dividido {cont} vezes')
else:
    print('\n\u001b[0mEle é primo')
