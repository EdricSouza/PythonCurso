#Estrutura de Repetição for
aula = 'Aula 13'
print(f'{aula:=^50}')

soma = 0
for c in range (0,3):
    valor = int(input('Digite um numero: '))
    soma = soma + valor
print(f'A soma é igual a {soma}')

vet = []
for c in range (0,5):
    vet.append(input('Digite um nome: '))
print(vet)