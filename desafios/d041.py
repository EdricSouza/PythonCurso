from datetime import date

#data
desafio = 'desafio 41'
print(f'{desafio:=^50}')

anonasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year

idade = ano - anonasc

if idade <= 9:
    print('Infantil')
elif idade <= 14:
    print('Mirim')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')