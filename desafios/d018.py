from math import sin, cos, tanh, radians

#sen, cos, tg
desafio = 'desafio 19'
print(f'{desafio:=^50}')

angulo = int(input('Digite o valor do ângulo: '))

seno = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tanh(radians(angulo))

print(f'O valor de seno, coseno e tangente do ângulo {angulo} é {seno:.2f}, {cose:.2f}, {tang:.2f} respectivamente')