from random import randint
from time import sleep

#Maior
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))
msg('Maior número')

list = []

def maiorAleatorio(list):
    print(f'Analisando os valores...')
    # sleep(3)
    for num in list:
        print(f'{num}', end = ' ')
    print(f'Foram informados {len(list)} números ao todo')
    maior = 0
    for num in list:
        if num > maior:
            maior = num
    print(f'O maior valor informado é {maior}')

n = randint(1, 10)

for a in range (1,n):
    for a in range (1,n):
        n = randint(1, 7)
        list.append(randint(1, 10))
    print('-'*20)
    maiorAleatorio(list)
    list.clear()



