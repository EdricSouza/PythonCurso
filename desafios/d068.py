from random import randint

#par ou impar
desafio = 'Desafio 68'
print(f'{desafio:=^50}')

r = 0
vit = 0
while True:
    print(f'------------{vit+1}ª Rodada------------')
    n = int(input("Digite um número:"))
    pc = randint(0,10)

    r = n + pc
    print(f'Você escolheu {n} e a máquina {pc}, {n} + {pc} = {r}, você ', end='')

    if r % 2 == 0:
        vit += 1
        print('venceu')
    else:
        print('perdeu')
        break
print('\n\n')
print(f'Sequencia de vitória: \u001b[32m{vit}\u001b[0m')
