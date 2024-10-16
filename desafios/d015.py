#aluguel de carros
desafio = 'desafio 15'
print(f'{desafio:=^50}')

km = float(input('Digite a quantia em quilometros rodados pelo carro: '))
dias = int(input('Digite por quantos dias ele foi alugado: '))

preco = (km * 0.15) + (60 * dias)

print(f'O preço final a ser pago por {dias} e {km} é de {preco:.2f}')