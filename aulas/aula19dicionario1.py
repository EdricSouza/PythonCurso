#Dicionários
aula = 'Aula 19'
print(f'{aula:=^50}')

brasil = []
estado = {'nome': 'Bahia', 'sigla': 'BA'}
estado2 = {'nome': 'Maranhâo', 'sigla': 'MA'}

brasil.append(estado)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])