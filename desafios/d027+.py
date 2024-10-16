#nome
desafio = 'desafio 27'
print(f'{desafio:=^50}')

nome = input('Digite seu nome completo: ').capitalize().strip()
nome = nome.split()

print(f'O primiro nome é: {nome[0]}')
print(f'O último nome é: {nome[len(nome)-1]}') # ou nome[-1]