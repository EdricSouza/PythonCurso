#formatação
aula = "Aula 7"
print(f'{aula:=^50}')

nome = input('Qual o seu nome: ')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:=^20}!')