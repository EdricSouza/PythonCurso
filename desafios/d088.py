from random import randint

#Sorteio
desafio = 'Desafio 88'
print(f'{desafio:=^50}')

numeros = []
numero = 0

quant = int(input('Quantos sorteios deseja fazer? '))
for cont in range(0, quant):
    numeros.clear()
    for i in range(0, 6):
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
    print(f'O {cont}° sorteio: {numeros}')
    numeros.clear()