#Desconto
desafio = 'desafio 12'
print(f'{desafio:=^50}')

valor = float(input('Digite o valor do produto: R$'))
valordes = valor * 0.95 #ou     valor - (valor * 5 / 100)

print(f'O valor com desconto do produto de {valor} é: {valordes:.2f}')