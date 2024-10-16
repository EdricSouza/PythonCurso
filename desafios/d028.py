import random

#random if
desafio = 'desafio 28'
print(f'{desafio:=^50}')

numero = random.randint(0,5)

input = int(input('Tente adivinhar o numero que a maquina pensou de 0 a 5: '))

if (input == numero):
    print('acertou')
else:
    print('tente novamente')