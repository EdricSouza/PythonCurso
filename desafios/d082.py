#par e impar
desafio = 'Desafio 82'
print(f'{desafio:=^50}')

numero = []
impar = []
par = []

while True:
    n = int(input('Digite um número: '))
    numero.append(n)
    if n % 2 == 0:
        impar.append(n)
    else:
        par.append(n)
    brk = input('Digite continuar? [N/S]').capitalize().strip()
    if brk[0] == 'N':
        break
    
print(f'Os ímpares são: {impar}')
print(f'Os pares são: {par}')