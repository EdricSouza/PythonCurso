from random import randint
from time import sleep

#Jogo
desafio = 'Desafio 91'
print(f'{desafio:=^50}')

posic = 1
jogo=dict()
for c in range (1,6):
    jogo[f"{c}° jogador"]=randint(1,6)

for k, v in jogo.items():
    print(f'{k} tirou: {v}')

rank = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('=-='*20)
for k, v in rank:

     print(f'{posic}o. lugar: {k} com {v}.')

     posic +=1

     sleep(1)