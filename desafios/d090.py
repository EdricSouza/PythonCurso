#Media
desafio = 'Desafio 90'
print(f'{desafio:=^50}')

aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média de {aluno['nome']}: '))
if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] <5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'

print('=-='*20)
for k,v in aluno.items():
    print(f'  - {k} é {v}')