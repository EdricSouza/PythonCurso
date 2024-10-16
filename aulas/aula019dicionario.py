#Dicionários
aula = 'Aula 19'
print(f'{aula:=^50}')

pessoas = {
    'nome': 'Edric',
    'idade': 22,
    'sexo': 'M'
}

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

pessoas['nome'] = 'Guilherme'
pessoas['peso'] = 70.6
del pessoas['sexo']

for k,v in pessoas.items():
    print(f'{k} = {v}')