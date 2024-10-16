#m e m
desafio = 'Desafio 65'
print(f'{desafio:=^50}')

maior = 0
menor = 0

n = int(input('Digite um valor: '))
maior = n
menor = n
media = 0
a = 0

opc = str(input('Deseja continuar? [S/N]').capitalize().strip())

while opc[0] == 'S':
    n = int(input('Digite outro valor: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    media += n
    a += 1
    opc = str(input('Deseja continuar? [S/N]').capitalize().strip())

print('____________________________________________')
print(f'A media entre esse valores é de: \u001b[33m{media/a}\u001b[0m')
print(f'O maior valor é: \u001b[32m{maior}\u001b[0m')
print(f'O menor valor é: \u001b[31m{menor}\u001b[0m')