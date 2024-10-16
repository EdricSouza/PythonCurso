#par ou impar
desafio = 'desafio 30'
print(f'{desafio:=^50}')

numero = int(input('digite um valor qualquer: '))

ver = numero % 2

print(ver)

if ver == 0:
    print('O número é par')
else:
    print('O número é ímpar')