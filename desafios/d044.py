#Pagamento
desafio = 'desafio 44'
print(f'{desafio:=^50}')

preco = float(input('Digite o preço do produto: '))
print('Digite a forma de pagamento \n1 - A vista (dinheiro)\n2 - A vista (cartão)\n3 - 2x no cartão\n4 - 3x ou mais no cartão\n')
opt = int(print('Digite a forma de pagamento: '))

if opt == 1:
    print(f'O preço do produto de R${preco} fica por R${preco - (preco * 0.1)}')
if opt == 2:
    print(f'O preço do produto de R${preco} fica por R${preco - (preco * 0.05)}')
if opt == 3:
    print(f'O preço do produto de R${preco} fica por R${preco}')
if opt == 4:
    print(f'O preço do produto de R${preco} fica por R${preco + (preco * 0.2)}')