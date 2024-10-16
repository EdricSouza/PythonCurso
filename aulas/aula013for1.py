#Estrutura de Repetição
aula = 'Aula 13'
print(f'{aula:=^50}')

numero = int(input('Digite um numero: '))
for c in range (0,numero+1,2):
    print(c)

inicio = int(input('Digite um numero: '))
fim = int(input('Digite um numero: '))
intervalo = int(input('Digite um numero: '))
for c in range (inicio,fim+1,intervalo):
    print(c)