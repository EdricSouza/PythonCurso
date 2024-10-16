#pa
desafio = 'desafio 51'
print(f'{desafio:=^50}')

ptermo = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

valor = ptermo
for c in range(0,10):
    print(valor)
    valor = valor + r