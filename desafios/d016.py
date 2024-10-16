from math import trunc as tr

#Truncar numero
desafio = 'desafio 16'
print(f'{desafio:=^50}')

numero = float(input('Digite um valor: '))

numerotruncado = numero.__trunc__()
print(f'O numero {numero} na forma arredondada é {numerotruncado}')