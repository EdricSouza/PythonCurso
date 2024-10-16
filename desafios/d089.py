#Media
desafio = 'Desafio 89'
print(f'{desafio:=^50}')

alunos = list()

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    brk = input('Deseja continuar? [S/N] ').upper().strip()
    if brk[0] == 'N':
        break

print('=-='*5,'MÉDIA','=-='*5)
print(f'N° Nome           Media')
for pos, detail in enumerate(alunos):
        
        print(f'{pos+1: <2} {detail[0]: <15} {detail[2]}')
