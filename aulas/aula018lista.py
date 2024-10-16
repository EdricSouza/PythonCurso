#Listas
aula = 'Aula 18'
print(f'{aula:=^50}')

teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 1

galera.append(teste[:])

print(galera)
print(teste)