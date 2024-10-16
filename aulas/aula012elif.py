#Condições aninhadas

aula = 'Aula 12'
print(f'{aula:=^50}')

nome = str(input('Digite seu nome: ')).capitalize()
if nome == 'Edric':
    print('Olá administrador!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Lucas':
    print('Olá novamente!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Olá garota!')
else:
    print('Seja bem vindo!')
print(f'Tenha um bom dia {nome}')