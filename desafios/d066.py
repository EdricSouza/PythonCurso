#soma
desafio = 'Desafio 66'
print(f'{desafio:=^50}')

v = 0
n = 0
while True:
    n = int(input('Digite o valor para soma [999 Para o código]: '))
    if n == 999:
        break
    v = n + v
     
print(f'\u001b[33mO valor da soma é igual a:\u001b[0m \u001b[32m{v}\u001b[0m')