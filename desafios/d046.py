from time import sleep
import emoji

#Temporizador
desafio = 'desafio 46'
print(f'{desafio:=^50}')

input('Pressione enter para dar início a contagem')

for t in range (10,0,-1):
    print(t)
    sleep(1)
print('0!!!')
print(emoji.emojize(':tada:',language='pt'))
