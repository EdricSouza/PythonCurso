# aumento
desafio = 'desafio 34'
print(f'{desafio:=^50}')

valor = float(input('Qual o valor de seu salário? '))

if valor > 1250:
    valor = valor * 1.10
else:
    valor = valor * 1.15

print(f'Seu novo salário é de R${valor}')