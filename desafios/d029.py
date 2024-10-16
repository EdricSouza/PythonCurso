from math import trunc

#radar eletronico
desafio = 'desafio 29'
print(f'{desafio:=^50}')

velocidade = float(input('Digite a velocidade em que o carro estava: '))

if velocidade > 80:
    excesso = trunc(velocidade) - 80
    multa = excesso*7
    #ou multa = (trunc(velocidade) - 80) * 7
    print(f'Você andou a {velocidade}km/h e por isso será multado em {multa} reais')
else:
    print(f'Você não foi multado por andar a {velocidade}km/h')