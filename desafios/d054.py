from datetime import datetime

#maioridade
desafio = 'desafio 54'
print(f'{desafio:=^50}')

maior = 0
menor = 0
for n in range (1,8):
    ano = int(input(f'Digite o ano de nascimento da {n}° pessoa: '))
    if datetime.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'A {maior} pessoas maior de idade e {menor} menor de idade')