# ano bissexto
desafio = 'desafio 32'
print(f'{desafio:=^50}')

ano = int(input('Digite o ano que deseja consultar: '))

if ano % 4 == 0:
    print(f'{ano} é ano bissexto')
else:
    print(f'{ano} Não é ano bissexto')