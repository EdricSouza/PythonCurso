#Dicionários
aula = 'Aula 19'
print(f'{aula:=^50}')

estado = dict()
brasil = list()
for cont in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')

for estado in brasil:
    for v in estado.values():
        print(f'{v} ', end='')
    print()