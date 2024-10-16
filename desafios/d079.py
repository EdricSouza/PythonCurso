#valor
desafio = 'Desafio 79'
print(f'{desafio:=^50}')

numeros = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in numeros:
        print('Valor já digitado')
    else:
        numeros.append(numero)
    
    brk = input('Deseja continuar? [S/N]').capitalize().strip()
    if brk[0] == 'N':
        break

numeros.sort()

print('Você digitou os seguintes números: ', end='')
for n in numeros:
    print(n, end='...')