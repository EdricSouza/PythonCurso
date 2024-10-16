from random import choice
#ramdom
desafio = 'desafio 19'
print(f'{desafio:=^50}')

aluno1 = input(f'Digite o nome do primeiro aluno: ')
aluno2 = input(f'Digite o nome do segundo aluno: ')
aluno3 = input(f'Digite o nome do terceiro aluno: ')
aluno4 = input(f'Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

alunoes = choice(lista)

print(f'Quem apagará o quadro será o {alunoes}')