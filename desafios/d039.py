from datetime import date

# Alistamento
desafio = 'desafio 39'
print(f'{desafio:=^50}')

anonasc = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
print (ano)

idade = ano - anonasc

if idade == 18:
    print('Você se alista esse ano')
elif idade < 18:
    tempo = 18 - idade
    print(f'ainda faltam {tempo} anos para o alistamento')
elif idade > 18:
    tempo = idade - 18
    print(f'Você devia ter se alistado a {tempo} ano atrás')