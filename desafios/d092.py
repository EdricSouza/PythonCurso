from datetime import datetime

#Aposentadoria
desafio = 'Desafio 92'
print(f'{desafio:=^50}')

pessoa = dict()

pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
pessoa['Idade'] = datetime.now().year - pessoa['Ano de Nascimento']
pessoa['Ctps'] = int(input('Carteira de Trabalho [0 se não tem]: '))
pessoa['Contratação'] = int(input('Ano de Contratação: '))
pessoa['Salario'] = float(input('Salário: R$'))


pessoa['Aposentadoria'] = 65 - pessoa['Contratação']

print('=-='*20)

for k, v in pessoa.items():
    print(f' -{k} tem o valor: {v}')