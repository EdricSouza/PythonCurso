# salario
desafio = 'desafio 36'
print(f'{desafio:=^50}')

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual é seu salário? '))
tempo = int(input('Em quantos anos você pretende pagar? '))

parcela = valor / tempo

if parcela > 0.3 * salario:
    print('Empréstimo negado')
else:
    print(f'As prestações ficarão no valor de {parcela}')