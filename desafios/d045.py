from random import randint
from time import sleep

#Pedra, papel e tesoura
desafio = 'desafio 45'
print(f'{desafio:=^50}')

option = ['pedra','papel','tesoura']
print("Selecione entre \n[0] Pedra\n[1] Papel\n[2] Tesoura")

opt = int(input('Selecione sua jogada: '))
pcopt = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')


print(f'Você selecionou {option[opt]} e o computador {option[pcopt]}')

if (opt == 0 and pcopt == 2) or (opt == 1 and pcopt == 0) or (opt == 2 and pcopt == 1):
    print('Você ganhou!')
elif opt == pcopt:
    print('Empate!')
else:
    print('A máquina ganhou!')