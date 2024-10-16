import math

#preco
desafio = 'desafio 31'
print(f'{desafio:=^50}')

distancia = int(input('Qual a distância em quilometros da sua viagem: '))

if distancia <= 250:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45
print(f'O valor será de: R${valor}')