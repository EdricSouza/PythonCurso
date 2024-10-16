from random import randint

#jogo
desafio = 'desafio 58'
print(f'{desafio:=^50}')

valor = randint(0,10)
opt = int(input('Tente advinhar o número: '))
tentativas  = 1
while opt != valor:
    opt = int(input('Incorreto! Tente novamente: '))
    tentativas += 1
print(f'Parabéns, você acertou o número escolhido em \u001b[32m{tentativas}\u001b[0m tentativas!!')