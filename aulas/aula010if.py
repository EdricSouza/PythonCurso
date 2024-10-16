#Condições

aula = 'Aula 10'
print(f'{aula:=^50}')

nome = input('Digite seu nome completo: ').capitalize().strip()
nome = nome.split()

if nome[0] == 'Edric':
    print(f'Olá novamente Edric!')
else:
    print(f'Seja bem vindo {nome[0]}')