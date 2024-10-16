#verificar letras
desafio = 'desafio 24'
print(f'{desafio:=^50}')

cidade = input('Digite a cidade em que você nasceu: ').lower().strip()

nome = cidade.split()
print(nome)
print('O resultado da consulta é:', 'santo' in nome[0])